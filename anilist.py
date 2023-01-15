import requests, re

ANILIST_URL = 'https://graphql.anilist.co'
 
CHARS_TO_REPLACE = r'[^a-zA-Z0-9:;.!_]'
CHARS_TO_REPLACE_WITH_UNDERSCORE = r'_?[^a-zA-Z0-9:;.!_]_?'

# querys for the first 10 favorite anime titles of a given user
def get_user_favorites(username):
    variables = {'name': username}
    query = '''
    query ($name : String) {
          User(name: $name) {
            favourites{
                anime(page:1, perPage: 10) {
                    nodes{
                        title {
                            romaji
                        }}}}}}
    '''
    result = requests.post(ANILIST_URL, json={'query': query, 'variables': variables}).json()
    return clean_response(result)

def get_all_anime(username):
    variables = {'name': username}
    query = '''
    query ($name : String) {
          User(name: $name) {
            statistics {
                anime {
                    scores(limit: 10, sort: MEAN_SCORE_DESC){
                        score,
                        mediaIds}}}}}
    '''
    result = requests.post(ANILIST_URL, json={'query': query, 'variables': variables}).json()
    return clean_response(result)

def clean_response(res):
    if "errors" in res:
        return None
    titles = res["data"]["User"]["favourites"]["anime"]["nodes"]
    for i, title in enumerate(titles):
        titles[i] = title["title"]["romaji"].replace(' ', '_')
        titles[i] = re.sub(CHARS_TO_REPLACE_WITH_UNDERSCORE, '_', titles[i])
        titles[i] = re.sub(CHARS_TO_REPLACE, '', titles[i])
        titles[i] = re.sub(r'_\Z', '', titles[i])
    return titles