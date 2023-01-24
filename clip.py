import anilist, sakugabooru
import requests
from sys import argv
from os import scandir, remove

CLIP_DIRECTORY = './clips/'

# Given an Anilist username, returns a list of links to 
# Sakugabooru mp4 files corresponding to that user's favorite Anime
def get_popular_clips(usr):
    shows = anilist.get_user_favorites(usr)
    mp4s = []
    for show in shows:
        mp4link = sakugabooru.sakuget_popular_mp4_link(50, show)
        if mp4link:
            mp4s.append(mp4link)
    return mp4s

# Downloads the mp4 from each link to clips/ directory
def download_clips(links):
    for link in links:
        response = requests.get(link[1])
        with open(f".{CLIP_DIRECTORY}{link[0]}.mp4", "wb") as f:
            f.write(response.content)

# Delete all files in clips/
def clear_clips():
    for file in scandir(CLIP_DIRECTORY):
        remove(file.path)
