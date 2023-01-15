import anilist, sakugabooru
import requests
from sys import argv

def get_popular_clips(usr):
    shows = anilist.get_user_favorites(usr)
    mp4s = []
    for show in shows:
        mp4link = sakugabooru.sakuget_popular_mp4_link(50, show)
        if mp4link:
            mp4s.append(mp4link)
    return mp4s

def download_clips(links):
    for link in links:
        response = requests.get(link[1])
        with open(f"./clips/{link[0]}.mp4", "wb") as f:
            f.write(response.content)

x = get_popular_clips(argv[1])
download_clips(x)
