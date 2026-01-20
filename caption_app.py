import os
import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import shutil
import socket
import time  # ← added for keeping alive

# Load BLIP model
print("Loading BLIP model... (first time ~20 seconds)")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
if torch.cuda.is_available():
    model = model.to("cuda")

# Base folder
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}
    out = model.generate(**inputs, max_length=100, num_beams=5)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption.strip()

def process_images(input_folder, trigger_word, add_trigger_position):
    if not os.path.isdir(input_folder):
        return "Error: Input folder not found. Please check the path.", None

    safe_trigger = trigger_word.strip().replace(" ", "_") or "captions"
    output_folder = os.path.join(BASE_FOLDER, f"{safe_trigger}_output")
    os.makedirs(output_folder, exist_ok=True)

    results = []
    image_files = sorted([f for f in os.listdir(input_folder) 
                          if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tiff"))])

    for filename in image_files:
        image_path = os.path.join(input_folder, filename)
        caption = generate_caption(image_path)
        
        if add_trigger_position == "Start":
            final_caption = f"{trigger_word} {caption}"
        elif add_trigger_position == "End":
            final_caption = f"{caption} {trigger_word}"
        else:
            final_caption = caption
        
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(output_folder, txt_filename)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(final_caption.strip())
        
        results.append(f"{filename}: {final_caption}")
    
    zip_path = os.path.join(BASE_FOLDER, f"{safe_trigger}_output.zip")
    shutil.make_archive(output_folder, 'zip', output_folder)
    
    progress = f"Processed {len(image_files)} images!\nOutput saved to: {output_folder}\n\n"
    return progress + "\n".join(results), zip_path

# Find available port
def find_available_port(start_port=7860, max_port=7870):
    for port in range(start_port, max_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                print(f"Using available port: {port}")
                return port
            except OSError:
                print(f"Port {port} in use, trying next...")
    print("No ports available in range. Falling back to random.")
    return None

# Gradio UI (same as before)
with gr.Blocks(title="Local Image Captioner (BLIP)") as demo:
    gr.Markdown("""
    # Local Image Captioner (BLIP Large)
    **Fully offline • RTX 3060 powered • No errors!**
    
    Paste your image folder path and add an optional trigger word.
    Generates .txt caption files + ZIP, all saved in this folder.
    """)
    
    with gr.Row():
        input_folder = gr.Textbox(label="Input Image Folder Path", placeholder=r"C:\Users\YourName\Pictures\dataset", scale=4)
        trigger_word = gr.Textbox(label="Trigger Word (optional)", placeholder="e.g., my_style", value="", scale=2)
    
    add_trigger_position = gr.Radio(["None", "Start", "End"], label="Trigger Position", value="Start")
    
    process_btn = gr.Button("🚀 Process All Images", variant="primary")
    
    output_text = gr.Textbox(label="Generated Captions", lines=15)
    output_zip = gr.File(label="📦 Download ZIP of Caption Files")
    
    process_btn.click(
        process_images,
        inputs=[input_folder, trigger_word, add_trigger_position],
        outputs=[output_text, output_zip]
    )
    
    gr.Markdown(f"**Outputs saved here:** `{BASE_FOLDER}`")

# Launch with auto-port + force browser open
available_port = find_available_port()
demo.launch(
    share=False,
    server_name="127.0.0.1",
    server_port=available_port,
    inbrowser=True,               # ← Force open default browser
    prevent_thread_lock=False     # Let launch block until stopped
)

# Keep the script alive (in case launch doesn't block)
print("\nGradio is running! Press Ctrl+C in this window to stop.")
try:
    while True:
        time.sleep(3600)  # Sleep forever, wake up every hour
except KeyboardInterrupt:
    print("Stopping Gradio...")