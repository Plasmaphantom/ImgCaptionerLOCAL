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
   git clone https://github.com/yourusername/local-image-captioner-blip.git
   cd local-image-captioner-blip
