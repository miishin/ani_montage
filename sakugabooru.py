import string, requests, os, ffmpeg
from random import choice
from json import dumps

# returns JSON response from querying the given tag with a given post # limit
def sakuget(num_posts, tag):
    p = {'limit': num_posts, 'tags': tag}
    r = requests.get('https://www.sakugabooru.com/post.json', params=p)
    return r.json()

# Returns the mp4 links in the JSON response
def get_mp4_links(r_json):
    return [json_object['file_url'] for json_object in r_json]

# Gets the most liked post out of the response
def get_most_popular(r_json):
    if not r_json:
        return None
    return max(r_json, key=lambda j: j['score']) 

# Filters the response for given file size (in bytes)
def filter_large_clips(r_json, max_file_size):
    if not r_json:
        return None
    return filter(lambda j: j['file_size'] < max_file_size, r_json)

# Test function to write json file locally
def sakuget_to_file(num_posts, tag):
    j = sakuget(num_posts, tag)
    with open("example.json", "w") as file:
        file.write(dumps(j))

# Query tag with post limit and file size limit so we don't get 1 minute long clips
def main(tag, num_posts, max_file_size):
    s = sakuget(num_posts, tag)
    if not s:
        return None
    s = filter_large_clips(s, max_file_size)
    post = get_most_popular(s)
    return (tag, post['file_url'])