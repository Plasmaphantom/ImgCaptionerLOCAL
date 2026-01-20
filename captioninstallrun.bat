@echo off
echo =================================================
echo   Local Image Captioner with BLIP (Stable Alternative)
echo   (RTX 3060 optimized - fully offline)
echo =================================================
echo.

cd /d "%~dp0"

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate.bat

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing PyTorch with CUDA...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

echo Installing gradio, transformers, pillow...
pip install gradio transformers pillow --quiet

if not exist caption_app.py (
    echo ERROR: caption_app.py not found!
    pause
    exit /b 1
)

echo.
echo Starting the Captioner App...
echo.
python caption_app.py

if errorlevel 1 (
    echo.
    echo Error occurred. Window stays open.
    pause
) else (
    echo.
    echo App closed normally.
    pause
)