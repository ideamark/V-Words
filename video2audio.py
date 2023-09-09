import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

from settings import audio_folder
from common import clear_folder, replace_ext, list_videos


clear_folder(audio_folder)
for video_path in list_videos():
    video_name = os.path.basename(video_path)
    audio_output_path = os.path.join(audio_folder, replace_ext(video_name, 'mp3'))
    ffmpeg_extract_audio(video_path, audio_output_path)