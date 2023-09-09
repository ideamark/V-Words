import os
import re
import json
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from settings import text_folder, output_folder
from common import int_to_time, list_videos, wrap_string, clear_folder
from add_subtitle import add_subtitle


def split_video(word='', explaination=''):
    for json_name in os.listdir(text_folder):
        json_path = os.path.join(text_folder, json_name)
        with open(json_path, 'r') as fp:
            js = json.load(fp)
            segments = js['segments']
            for segment in segments:
                text = segment['text'].lower()
                if word in text.split(' '):
                    start = segment['start'] - 0.4
                    end = segment['end'] + 0.4
                    if end - start > 1.0:
                        start_time = int_to_time(start)
                        end_time = int_to_time(end)
                        result = text.replace(word, f'[ {word} ]')
                        print(f'[{start_time}, {end_time}] {result}')
                        base_name = os.path.splitext(json_name)[0]
                        video_path = ''
                        for video in list_videos():
                            if base_name in os.path.basename(video):
                                video_path = video
                                break
                        if video_path:
                            sub_folder = re.sub(r'[^a-zA-Z0-9]', '_', word)
                            sub_path = os.path.join(output_folder, sub_folder)
                            if not os.path.exists(sub_path):
                                os.mkdir(sub_path)
                            output_video_path = os.path.join(sub_path, f'{base_name}_({start_time}-{end_time}).mp4')
                            ffmpeg_extract_subclip(video_path, start, end, output_video_path)
                            subtitle = wrap_string(result) + '\n' + wrap_string(explaination)
                            add_subtitle(output_video_path, subtitle)


if __name__ == '__main__':
    word = 'absent'
    explaination = 'a.缺席的'
    clear_folder(output_folder)
    split_video(word, explaination)