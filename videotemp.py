import streamlit as st
import subprocess
import os

def convert_vtt_to_ass(vtt_path, ass_path):
    """Convert VTT to ASS with left-aligned subtitles using Mukta font."""
    ass_template = """[Script Info]
Title: Styled Subtitles
ScriptType: v4.00+
Collisions: Normal
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Mukta,40,&H00FFFFFF,&H000000,&H000000,-1,0,1,2,2,70,70,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    def convert_time(vtt_time):
        h, m, s = vtt_time.split(":")
        s, ms = s.split(".")
        ms = ms[:2]  # Keep two decimal places
        return f"{h}:{m}:{s}.{ms}"

    with open(vtt_path, "r", encoding="utf-8") as vtt, open(ass_path, "w", encoding="utf-8") as ass:
        ass.write(ass_template)
        lines = vtt.readlines()

        for i in range(len(lines)):
            if "-->" in lines[i]:
                start, end = lines[i].strip().split(" --> ")
                start = convert_time(start)
                end = convert_time(end)
                text = lines[i + 1].strip() if i + 1 < len(lines) else ""
                if text:
                    ass.write(f"Dialogue: 0,{start},{end},Default,,0,0,0,,{text}\n")

def burn_subtitles(vtt_file, photo, audio, output):
    ass_path = "subtitles.ass"
    convert_vtt_to_ass(vtt_file, ass_path)

    temp_bg_video = "background.mp4"
    waveform_video = "waveform.mp4"
    overlay_video = "overlay.mp4"
    final_video = "final.mp4"

    # Step 1: Create Background Video
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=black:s=1920x1080:duration=194",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", temp_bg_video
    ], check=True)

    # Step 2: Create Waveform Video
    subprocess.run([
        "ffmpeg", "-y", "-i", audio, 
        "-filter_complex", "[0:a]showwaves=s=1920x100:mode=line:colors=white[v]", 
        "-map", "[v]", "-c:v", "libx264", "-pix_fmt", "yuv420p", waveform_video
    ], check=True)

    # Step 3: Overlay Image on Background
    subprocess.run([
        "ffmpeg", "-y", "-i", temp_bg_video, "-i", photo,
        "-filter_complex", "[1:v]scale=960:-1,pad=960:1080:(ow-iw)/2:(oh-ih)/2[photo];[0:v][photo]overlay=960:0",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", overlay_video
    ], check=True)

    # Step 4: Burn Subtitles and Overlay Waveform
    subprocess.run([
        "ffmpeg", "-y", "-i", overlay_video, "-i", waveform_video,
        "-filter_complex", f"[0:v][1:v]overlay=0:0[v];[v]ass={ass_path}",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", final_video
    ], check=True)

    # Step 5: Add Audio
    subprocess.run([
        "ffmpeg", "-y", "-i", final_video, "-i", audio,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", output
    ], check=True)

    st.success(f"Video generated successfully: {output}")

st.title("Video Generator 🎥 with Audio & Subtitles")

vtt_file = st.file_uploader("Upload Subtitle File (VTT)", type=["vtt"])
image_file = st.file_uploader("Upload Background Image (JPG/PNG)", type=["jpg", "png"])
audio_file = st.file_uploader("Upload Audio File (MP3)", type=["mp3"])
output_name = st.text_input("Output Video Filename", "output.mp4")

if st.button("Generate Video"):
    if vtt_file and image_file and audio_file and output_name:
        with open("uploaded_vtt.vtt", "wb") as f:
            f.write(vtt_file.read())
        with open("uploaded_image.jpg", "wb") as f:
            f.write(image_file.read())
        with open("uploaded_audio.mp3", "wb") as f:
            f.write(audio_file.read())

        burn_subtitles("uploaded_vtt.vtt", "uploaded_image.jpg", "uploaded_audio.mp3", output_name)

    else:
        st.error("⚠️ Please upload all files and provide the output filename.")
