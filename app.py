import clip, vidmerge
import title_card_generator as tcg
import argparse

# Usage:
# app.py [--user USERNAME, --style STYLE]
# STYLE: ["EVA", "BEBOP"]
def main():

    parser = argparse.ArgumentParser(description="AniList to montage. Enter an AniList username and a style: one of [EVA, BEBOP]")
    parser.add_argument("--user", help="AniList username")
    parser.add_argument("--style", help="Titlecard style")
    args = parser.parse_args()

    clip.clear_clips()
    vidmerge.clear_clean_clips()
    
    username = args.user
    title_card = args.style
    if title_card is None:
        title_card = "bebop"

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
