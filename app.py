import clip, vidmerge
import title_card_generator as tcg
from sys import argv

# Usage:
# app.py [username] [title_card_type]
# title card type: 0 - bebop, 1 - eva
def main():
    clip.clear_clips()
    vidmerge.clear_clean_clips()

    print("Grabbing video links")
    mp4links = clip.get_popular_clips(argv[1])
    print("Downloading videos!")
    clip.download_clips(mp4links)
    print("Generating title card")
    tcg.main(argv[1], argv[2])
    print("Generating reel")
    vidmerge.combine_clips()
    print("Done!")

if __name__ == '__main__':
    main()
