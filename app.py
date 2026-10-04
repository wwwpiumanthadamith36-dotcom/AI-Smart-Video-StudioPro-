import PIL.Image
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

import streamlit as st
import google.generativeai as genai
import yt_dlp
import whisper
import gtts

# MoviePy Import Fix
try:
    from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
    import moviepy.video.fx.all as vfx
except Exception:
    from moviepy.video.io.VideoFileClip import VideoFileClip
    from moviepy.audio.io.AudioFileClip import AudioFileClip
    from moviepy.audio.AudioClip import concatenate_audioclips
    import moviepy.video.fx as vfx

import os
import tempfile
import gc
