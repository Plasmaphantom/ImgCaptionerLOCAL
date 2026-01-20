# ImgCaptionerLOCAL
Localhosted Image captioner for ComfyUI or FLUXgym
# Local Image Captioner (BLIP)

A simple, **100% offline**, GPU-accelerated image captioning tool built for Windows users with NVIDIA GPUs (tested on RTX 3060).

Perfect for quickly generating high-quality captions for large image datasets — especially useful for preparing training data for LoRA, DreamBooth, fine-tuning Stable Diffusion / Flux models, or any other image-to-text task where you want full privacy and no cloud dependency.

### Features
- Uses **Salesforce/blip-image-captioning-large** — reliable, natural-sounding captions
- RTX 3060 / CUDA acceleration → ~1–3 seconds per image
- Gradio web interface (localhost only)
- Drag-and-drop style workflow: paste folder path → add optional trigger word → process
- Automatically creates output folder + ZIP archive with .txt caption files
- Trigger word support (add at start/end/none) — great for consistent dataset formatting
- One-click setup via batch file (creates venv, installs everything)

### Why this tool?
Many online captioning services (or even some local tools) either:
- Require uploading images to the cloud
- Have complicated dependencies / error-prone setups (looking at you, Florence-2)
- Are too slow on CPU

This one is:
- Fully private (everything stays on your machine)
- Easy to run for non-technical users (double-click .bat → done)
- Portable — just move the folder anywhere

### Requirements
- Windows (tested on 10/11)
- NVIDIA GPU with ≥8 GB VRAM (RTX 3060 works great)
- Python 3.8+ installed[](https://www.python.org/downloads/)
- ~5–10 GB free disk space (first run downloads model + packages)

### Installation & Usage

1. **Clone or download** this repository

   ```bash
   git clone https://github.com/Plasmaphantom/local-image-captioner-blip.git
   cd local-image-captioner-blip

   Or just download ZIP and extract.

Double-click start_captioner.bat
First run: creates virtual environment + downloads ~1.5 GB of model/weights (takes 3–10 min depending on internet)
Subsequent runs: starts in seconds

In the browser window that opens:
Paste your images folder path (e.g. C:\Users\Hunter\Pictures\my_dataset)
(Optional) Enter a trigger word (e.g. my_style, tok)
Choose where to place the trigger (Start / End / None)
Click Process All Images

Results appear in the same folder as the .bat file:
New subfolder: triggerword_output/
ZIP file: triggerword_output.zip
Each image gets a matching .txt file with the caption

Example Output
textimage001.jpg → "a beautiful sunset over the mountains my_style"
image002.png → "my_style portrait of a woman smiling in a park"

Troubleshooting

Black window closes immediately? → Make sure Python is installed and added to PATH
CUDA errors? → Confirm your GPU drivers are up to date (NVIDIA Game Ready or Studio drivers)
Slow on CPU? → Normal if no CUDA — captions will still work, just slower
Still stuck? Open an issue or paste the error from the command window.

Want better captions?
This version uses BLIP-large because it's stable and easy to install.
This is my 2nd repository (I am still learning how this stuff works but wanted to contribute to anyone having trouble with captioning their datasets)

Just let me know in issues/PRs.
License
MIT License — feel free to use, modify, share.
Happy captioning! 🚀
Made with love for the local AI community.
