# Overview
Python script that allows users to download audio from YouTube videos. It provides a simple command-line interface (CLI) and a graphical user interface (GUI) built with tkinter, it takes the URL, downloads the YT video and change the extension to mp3, and finally places it on the folder set as 'MUSIC' environment. If you have the folder path added to your Spotify to show the songs as local files, the songs downloaded will be automatically added to the Local files playlist.

# Features
- Download audio from YouTube videos by providing either the video.
- Converts downloaded videos to MP3 audio format.
- Moves the downloaded audio files to a specified folder.

# Imports

- yt_dlp
- tkinter
- shutil

# Installation
1. Clone the repository to your local machine:

```
git clone https://github.com/your_username/youtube_audio_downloader.git
```

2. Run the script on your local (remember that you should set MUSIC env to an existing file in your PC)
