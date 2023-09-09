# V-Words

## 综述

V-Words 是一款单词视频制作工具，支持 Windows, Linux, MacOS. 可以从海量的视频文件中自动截取视频片段，制作出单词短视频。

效果如下：

[![Video Preview](https://img.youtube.com/vi/Z7-Wk-5Ed5E/0.jpg)](https://youtu.be/Z7-Wk-5Ed5E)

## 安装

* 下载安装 [ffmpeg](https://ffmpeg.org/download.html), [ImageMagick](https://imagemagick.org/script/download.php)

  * 备注：windows下的安装向导需要勾选 `install legacy utilities`.
* 安装 `pytorch`
* 安装剩余模块：`pip install -r requirements.txt`

## 使用

1. 配置 `settings.py` 文件，设置原始视频路径 `video_path`
2. 首先运行 `video2audio.py`，批量提取原始视频的音频到 `audio` 文件夹
3. 然后运行 `audio2text.py`，将音频批量转化为 json文本，存于 `text` 文件夹
4. 最后运行 `run.py`，按照 `words.csv` 中的单词和释义，批量生成单词视频片段至 `split_videos` 文件夹

## 联系方式

* 作者：Mark Yang
* 邮箱：ideamark@qq.com
