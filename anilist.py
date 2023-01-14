import requests, re

ANILIST_URL = 'https://graphql.anilist.co'

# Sakugabooru likes: ! - ; 
GOOD_CHARACTERS = r'[!-;\']'
# doesn't like .
BAD_CHARACTERS = r'[.]'

# querys for the first 10 favorite anime titles of a given user
def get_user(username):
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
    return result

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
    return result

def clean_response(res):
    if "errors" in res:
        return None
    titles = res["data"]["User"]["favourites"]["anime"]["nodes"]
    for i, title in enumerate(titles):
        s = re.sub()
        titles[i] = re.sub(r'\W+', '', title["title"]["romaji"].replace(' ', '_'))
    return titles



