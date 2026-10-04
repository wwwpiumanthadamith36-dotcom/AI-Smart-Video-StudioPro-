try:
    from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
    import moviepy.video.fx.all as vfx
except ImportError:
    from moviepy.video.io.VideoFileClip import VideoFileClip
    from moviepy.audio.io.AudioFileClip import AudioFileClip
    from moviepy.audio.AudioClip import concatenate_audioclips
    import moviepy.video.fx as vfx
