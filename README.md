# V-Words

## Summary

V-Words is a word video clip maker, which can make word short videos from amount of video files. Supports Windows, Linux, MacOS.

Demo:

[![Video Preview](https://img.youtube.com/vi/Z7-Wk-5Ed5E/0.jpg)](https://youtu.be/Z7-Wk-5Ed5E)

## Installation

* Download and install [ffmpeg](https://ffmpeg.org/download.html), [ImageMagick](https://imagemagick.org/script/download.php)

  * Note: For windows, in the installation wizard you need to select `install legacy utilities`.
* Install `pytorch`
* Install residual modules: `pip install -r requirements.txt`

## Usage

1. Config `settings.py` to set the input video path: `video_path`
2. Make sure srt files and videos are in the same path.
3. Run `video2audio.py` to extract audio from input videos into folder `audio`
4. Run `run.py`，refer to the words in `words.csv` to generate video clips into folder `output`

## Contact

* Author: Mark Yang
* Email: ideamark@qq.com
