import os
import re
import pysrt
from moviepy.editor import VideoFileClip

from settings import output_folder, video_folder
from common import time_to_seconds, list_dir, wrap_string, clear_folder
from add_subtitle import add_subtitle


def split_video(word='', explaination=''):
    srt_ext = '.srt'
    for srt_file in list_dir(video_folder, [srt_ext]):
        subtitles = []
        try:
            subtitles = pysrt.open(srt_file)
        except Exception:
            print(f'Can not parse {srt_file}')
        for subtitle in subtitles:
            text = subtitle.text.lower()
            if word in text.split(' '):
                start_time = subtitle.start
                end_time = subtitle.end
                start = time_to_seconds(start_time)
                end = time_to_seconds(end_time)
                result = text.replace(word, f'[ {word} ]')
                print(f'[{start_time}, {end_time}] {result}')
                base_name = os.path.basename(srt_file).split(srt_ext)[0]
                video_path = ''
                for video in list_dir(video_folder, ['.mp4', '.mkv', '.wmv']):
                    if base_name in os.path.basename(video):
                        video_path = video
                        break
                if video_path:
                    sub_folder = re.sub(r'[^a-zA-Z0-9]', '_', word)
                    sub_path = os.path.join(output_folder, sub_folder)
                    if not os.path.exists(sub_path):
                        os.mkdir(sub_path)
                    ext = os.path.splitext(video_path)[-1]
                    output_video_path = os.path.join(sub_path, f'{base_name}_({start_time}-{end_time}){ext}'.replace(":", "_").replace(",", "_"))
                    video_clip = VideoFileClip(video_path)
                    sub_clip = video_clip.subclip(start, end)
                    sub_clip.write_videofile(output_video_path, codec='libx265')
                    sub_clip.close()
                    new_subtitle = wrap_string(result) + '\n' + wrap_string(explaination)
                    add_subtitle(output_video_path, new_subtitle)


if __name__ == '__main__':
    word = 'to'
    explaination = 'prep. 朝；位于'
    clear_folder(output_folder)
    split_video(word, explaination)