import os
from datetime import datetime
import textwrap

from settings import video_folder


def get_duration(index):
    start_time = index * 5
    end_time = (index + 1) * 5
    return start_time, end_time


def time_to_seconds(time, time_format='%H:%M:%S,%f'):
    ref_dt = datetime(1900, 1, 1, 0, 0, 0)
    time = datetime.strptime(str(time), time_format) - ref_dt
    return time.seconds + time.microseconds / 1000000


def clear_folder(folder):
    if os.listdir(folder):
        if os.name == 'nt':
            os.system(f'del /q /s "{folder}\*"')
        else:
            os.system(f'rm -rf {folder}/*')


def replace_ext(filename, new_extension):
    root, _ = os.path.splitext(filename)
    new_filename = f'{root}.{new_extension}'
    return new_filename


def list_videos(root_dir=video_folder):
    def is_video_file(file):
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
        _, extension = os.path.splitext(file)
        return extension.lower() in video_extensions
    video_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if is_video_file(file):
                file_path = os.path.join(root, file)
                video_files.append(file_path)
    return video_files


def wrap_string(text, max_length=50):
    wrapper = textwrap.TextWrapper(width=max_length)
    wrapped_text = wrapper.fill(text)
    return wrapped_text


if __name__ == '__main__':
    print(list_videos(video_folder))