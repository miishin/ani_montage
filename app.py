import clip, vidmerge
import title_card_generator as tcg
from sys import argv

# Usage:
# app.py [username] [title_card_type]
# title card type: "eva" or "bebop" for now
def main():
    clip.clear_clips()
    vidmerge.clear_clean_clips()
    
    username = argv[1]
    title_card = argv[2]

    print("Grabbing video links")
    mp4links = clip.get_popular_clips(username)
    print("Downloading videos!")
    clip.download_clips(mp4links)
    print("Generating title card")
    tcg.main(username, title_card)
    print("Generating reel")
    vidmerge.combine_clips()
    print("Done!")

if __name__ == '__main__':
    main()
