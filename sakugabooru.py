import string
import requests
import os
from random import choice
from json import load, dumps

# returns JSON response from querying the given tag
def sakuget(num_posts, tag):
    p = {'limit': num_posts, 'tags': tag}
    r = requests.get('https://www.sakugabooru.com/post.json', params=p)
    return r.json()

# sorts the json response
def sort_posts(posts):
    return sorted(posts, key=lambda p: p['score'], reverse=True)


sort_posts(sakuget(1, "One_Piece"))
# grabs the links to the mp4
def get_mp4_links(r_json):
    links = []
    for json_obj in r_json:
        links.append(json_obj['file_url'])
    return links

def get_most_popular(r_json):
    hs = -1
    best = None
    for json_obj in r_json:
        if json_obj['score'] > hs:
            hs = json_obj['score']
            best = json_obj
    return best

    
def sakuget_popular_mp4_link(num_posts : int, search_tag : string):
    clip = get_most_popular(sakuget(num_posts, search_tag))
    if clip:
        return clip['file_url']
    return clip



    
