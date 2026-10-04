import streamlit as st

# Page Configuration - මෙය පළමු පේළිය ලෙසම තිබිය යුතුය
st.set_page_config(page_title="AI Smart Video Studio Pro 🇱🇰", page_icon="🇱🇰", layout="wide")

import os
import tempfile
import gc
import PIL.Image
import google.generativeai as genai
import yt_dlp
import whisper
import gtts

try:
    from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
    import moviepy.video.fx.all as vfx
except Exception:
    from moviepy.video.io.VideoFileClip import VideoFileClip
    from moviepy.audio.io.AudioFileClip import AudioFileClip
    from moviepy.audio.AudioClip import concatenate_audioclips
    import moviepy.video.fx as vfx
