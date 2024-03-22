import os
import requests
import yt_dlp
import shutil
import time
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import  messagebox

# Set MUSIC var and point to the folder to save the mp3 files
os.environ['MUSIC'] = r'D:\Music'


def download(url):
    print(f"URL: {url}")

    try:
        # download the video 
        
        with yt_dlp.YoutubeDL({'format': 'bestaudio', 'outtmpl': '%(title)s.%(ext)s', 'noplaylist' : True}) as ydl:
            info_dict = ydl.extract_info(url, download=True)

        # get the filename of the downloaded file to use as a filename
        filename = ydl.prepare_filename(info_dict)
        print(f"Downloaded file: {filename}")

        # convert the file to MP3 format
        mp3_filename = filename[:-4] + '.mp3'  # changes the extension to mp3
        shutil.move(filename, mp3_filename)
        print(f"Converted to MP3: {mp3_filename}")

        # move the MP3 file to the MUSIC folder
        destination = os.path.join(os.getenv("MUSIC"), os.path.basename(mp3_filename))
        shutil.move(mp3_filename, destination)
        print(f"Moved file to {destination}")
        
        return destination
    
    except Exception as e:
        print(f"Error downloading/moving file: {e}")
        return None

def main(query):
    file = None

    if not os.getenv("MUSIC"):
        print("Please export the environment variable MUSIC. Exiting...")
        exit()

    if "https://" in query and 'youtube' in query and 'watch' in query:
        file = download(query)

    elif file is None:
        print("Error occurred during download. Exiting..")
        quit()

    print(f"Got file: {file}")

    # Wait for the file to be moved
    while not os.path.exists(file):
        time.sleep(1)

    if os.path.exists(file):
        print("File successfully downloaded and moved.")
        messagebox.showinfo("Success", "Download successful!")
        root.destroy() #close the tkinter window if the download is successful
    else:
        print("File not found. Exiting...")
        quit()

def start_download():
    query = entry.get()
    main(query)

# Create a GUI window using tkinter
root = tk.Tk()
root.title("YouTube Audio Downloader")

# Create a label
label = tk.Label(root, text="Enter video URL or search query:")
label.pack()

# Create an entry field
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button to start the download process
button = tk.Button(root, text="Download", command=start_download)
button.pack()

# Run the GUI
root.mainloop()