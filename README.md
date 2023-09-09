# V-Words

## Summary

V-Words is a word video clip maker, which can make word short videos from amount of video files. Supports Windows, Linux, MacOS.

Demo:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Z7-Wk-5Ed5E?si=mgD9SGVXOQ8Bp-3a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Installation

* Download and install [ffmpeg](https://ffmpeg.org/download.html), [ImageMagick](https://imagemagick.org/script/download.php)

  * Note: For windows, in the installation wizard you need to select `install legacy utilities`.
* Install `pytorch`
* Install residual modules: `pip install -r requirements.txt`

## Usage

1. Config `settings.py` , set the origin videos path `video_path`
2. Firstly, run `video2audio.py` to extract audio from original videos into folder `audio`
3. Secondly, run `audio2text.py` to transfer audio files into json text files into folder `text`
4. Finally, run `run.py`，refer to the words in `words.csv` to generate video clips into folder  `split_videos`

## Contact

Author: Mark Yang
Email: ideamark@qq.com
