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
def sort_posts(posts, key, desc):
    return sorted(posts, key=lambda p: p[key], reverse=desc)

# grabs the links to the mp4
def get_mp4_links(r_json):
    links = []
    for json_obj in r_json:
        links.append(json_obj['file_url'])
    return links

def get_most_popular(r_json):
    if not r_json:
        return None
    return max(filter_long_clips(r_json), key=lambda j: j['score']) 

def filter_long_clips(r_json):
    if not r_json:
        return None
    return filter(lambda j: j['file_size'] < 10000000, r_json)

def sakuget_popular_mp4_link(num_posts : int, search_tag : string):
    clip = get_most_popular(sakuget(num_posts, search_tag))
    if clip:
        return (search_tag, clip['file_url'])
    return None