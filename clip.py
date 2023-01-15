import anilist, sakugabooru
from sys import argv

def get_popular_clips(usr):
    shows = anilist.get_user_favorites(usr)
    mp4s = []
    for show in shows:
        mp4link = sakugabooru.sakuget_popular_mp4_link(50, show)
        if mp4link:
            mp4s.append(mp4link)
    return mp4s

print(get_popular_clips(argv[1]))