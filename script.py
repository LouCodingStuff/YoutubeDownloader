import urllib.request
import importlib
import subprocess
import os

# check if pytube is installed
try:
    importlib.import_module('pytube')
except ImportError:
    # install pytube
    subprocess.check_call(['pip', 'install', 'pytube'])

from pytube import YouTube

# ask user for video URL
video_url = input("Enter the YouTube video URL: ")

# create YouTube object
yt = YouTube(video_url)

# get highest resolution stream
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# download video
print("Downloading video...")
video_file = stream.download()

# create folder with video title
video_title = yt.title
video_folder = video_title.replace('/', '_')
os.makedirs(video_folder, exist_ok=True)

# move video to folder
video_path = os.path.join(video_folder, os.path.basename(video_file))
os.rename(video_file, video_path)

# download thumbnail
thumbnail_url = yt.thumbnail_url
thumbnail_file = os.path.join(video_folder, video_title + '.jpg')
print("Downloading thumbnail...")
urllib.request.urlretrieve(thumbnail_url, thumbnail_file)
print("Download complete!")

print("Video and thumbnail downloaded successfully in folder:", video_folder)

