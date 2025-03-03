# Video Generator Streamlit App

## Overview
The **Video Generator Streamlit App** is a web-based tool built with **Streamlit** and **FFmpeg** that allows users to create and process videos in two ways:

1. **Video Creation (Tab 1):** Generate a video with a black background, a photo on the right, subtitles from a VTT file on the left, a waveform at the top, and synchronized audio from an MP3 file.
2. **Add Logo to Video (Tab 2):** Overlay a logo (PNG) onto an existing MP4 video at a customizable position and scale.

This app is ideal for content creators, educators, and developers who need to produce videos with dynamic elements like subtitles, images, audio, waveforms, and logos.

## Features
### Video Creation:
- Supports **VTT subtitles**, **JPG/PNG images**, and **MP3 audio**.
- Displays a **white waveform** at the top, a photo on the right (**960x1080**), and left-aligned subtitles using the **Mukta font**.
- Outputs a **1920x1080 MP4 video** with synchronized audio.

### Logo Addition:
- Adds a **PNG logo** to an **MP4 video** at user-specified positions (**top-left, top-right, bottom-left, bottom-right, center**).
- Allows scaling of the logo (**0.01 to 0.5** of its original size, default **0.08**).
- Preserves the **original audio and video quality**.

### User-Friendly Interface:
- Streamlit-based **web interface** with file uploaders, position selectors, sliders, and progress feedback.
- Downloadable output videos after processing.

## Prerequisites
To use this app locally, you need:

- **Python 3.8+**
- **FFmpeg** installed on your system:
  - Windows: `choco install ffmpeg` (using Chocolatey) or download from [FFmpeg.org](https://ffmpeg.org/).
  - Linux: `sudo apt-get install ffmpeg` (Ubuntu/Debian) or equivalent for your distribution.
  - macOS: `brew install ffmpeg` (using Homebrew).
- **Streamlit**: Install via `pip install streamlit`.

## Installation
Clone or download this repository:

```bash
git clone https://github.com/your-username/video-processing-streamlit.git
cd video-processing-streamlit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` contains:

```text
streamlit
```

Verify FFmpeg is installed by running:

```bash
ffmpeg -version
```

## Usage
### Running Locally
Navigate to the project directory and run the Streamlit app:

```bash
streamlit run app.py
```

Open the app in your web browser (default: **http://localhost:8501**).

### App Tabs
#### Tab 1: Video Creation
1. Upload a **.vtt** subtitle file, **.jpg/.png** image, and **.mp3** audio file.
2. Specify an **output video filename** (e.g., `Check-New-Output-Tyrst-with-Destiny-Back.mp4`).
3. Click **“Generate Video”** to process the video.
4. Download the resulting **MP4 video**.

#### Tab 2: Add Logo to Video
1. Upload an **.mp4** video file and a **.png** logo file.
2. Specify an **output video filename** (e.g., `New-template-video.mp4`).
3. Choose the **logo position** and adjust the **scale factor**.
4. Click **“Add Logo”** to process the video.
5. Download the resulting **MP4 video**.

## Example Inputs
### Tab 1 Inputs:
- `transcription.vtt`: WebVTT subtitle file.
- `Jnehru.jpg`: JPG image for the right side.
- `A Tryst with Destiny.mp3`: MP3 audio file.
- Output: `Check-New-Output-Tyrst-with-Destiny-Back.mp4`

### Tab 2 Inputs:
- `Check.mp4`: MP4 video file.
- `suvichaarwhitelogoprimaryhori.png`: PNG logo image.
- Output: `New-template-video.mp4`

## Deployment
### Local Deployment
Follow the **installation** and **usage** steps above. Ensure **FFmpeg** is installed locally.

### Streamlit Cloud Deployment (Limited)
Streamlit Cloud’s free tier doesn’t support **FFmpeg** installation, so full functionality is not possible.

### Alternative Deployment Platforms
For full deployment, use platforms like **Heroku**, **AWS**, or **Google Cloud** where FFmpeg can be installed. Steps:
1. Push your code to GitHub.
2. Set up a server with FFmpeg installed.
3. Create a Dockerfile or use a virtual machine for deployment.

## Contributing
1. Fork this repository.
2. Create a branch for your feature or bug fix.
3. Submit a pull request with your changes.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Built with **Streamlit** for the web interface.
- Uses **FFmpeg** for video processing.
- Inspired by video creation and logo overlay needs for content production.
