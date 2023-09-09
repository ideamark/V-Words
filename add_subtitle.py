import os
from moviepy.editor import *
from moviepy.video.VideoClip import TextClip


def add_subtitle(video_path, text):
    video_temp_path = f'{video_path}_temp'
    if os.name == 'nt':
        os.system(f'move {video_path} {video_temp_path}')
    else:
        os.system(f'mv {video_path} {video_temp_path}'.replace("(", r"\(").replace(")", r"\)"))
    
    font = 'song.ttf'
    font_size = 40
    font_color = 'white'

    video = VideoFileClip(video_temp_path)
    text_clip = TextClip(text, fontsize=font_size, font=font, color=font_color).set_duration(video.duration)

    video_width, video_height = video.size
    text_x = (video_width - text_clip.w) / 2
    text_y = (video_height - text_clip.h) / 2
    text_clip = text_clip.set_position((text_x, text_y))
    
    result = CompositeVideoClip([video, text_clip])
    result.write_videofile(video_path, codec='libx264', audio_codec='aac')
    if os.name == 'nt':
        os.system(f'del {video_temp_path}')
    else:
        os.system(f'rm {video_temp_path}'.replace("(", r"\(").replace(")", r"\)"))


if __name__ == '__main__':
    add_subtitle('output/test.mp4', '你好啊世界！')


