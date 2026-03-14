#!/usr/bin/env python3
import os
import shutil

folders = ["images", "music", "videos", "documents", "links"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

shutil.copy("/home/justinsunday/Downloads/picture.jpg", "images/picture.jpg")
shutil.copy("/home/justinsunday/Downloads/song.mp3", "music/song.mp3")
shutil.copy("/home/justinsunday/Downloads/video.mp4", "videos/video.mp4")
shutil.copy("/home/justinsunday/Documents/report.pdf", "documents/report.pdf")

link = "https://github.com"
with open("links/links.txt", "a") as file:
    file.write(link + "\n")

print("Files and links saved successfully!")
