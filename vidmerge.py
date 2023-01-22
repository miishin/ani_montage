import ffmpeg
import os

CLIP_DIRECTORY = "./clips/"
CLEAN_CLIP_DIRECTORY = "./clean_clips/"
CLIP_FILES = os.listdir(CLIP_DIRECTORY)
VIDEO_WIDTH = 854
VIDEO_HEIGHT = 480
TITLE_CARD_FILE = "title.png"
TITLE_CARD_VIDEO = "title.mp4"
def open_files():
    return [ffmpeg.input(CLEAN_CLIP_DIRECTORY + file) for file in CLIP_FILES]

# edit all the clips to a desired resolution and fps and dump in clean_clips/ directory
def sanitize_clips():
    for file in CLIP_FILES:
        (
            ffmpeg.input(os.path.join(CLIP_DIRECTORY, file))
            .filter("scale", size="%d:%d" % (VIDEO_WIDTH, VIDEO_HEIGHT))
            .filter('fps', fps=24, round='up')
            .output(CLEAN_CLIP_DIRECTORY + file)
            .run()
        )

# delete files in /clean_clips
def clear_clean_clips():
    for file in os.scandir(CLEAN_CLIP_DIRECTORY):
        os.remove(file.path)

# combines the clips into one montage
def combine_clips():
    sanitize_clips()
    v_files = [f.video for f in open_files()]
    #v_files = [item for sublist in map(lambda f: [f.video, f.audio], open_files()) for item in sublist]
    print(v_files)
    try:
        if os.path.isfile(TITLE_CARD_FILE):
            ffmpeg.input(TITLE_CARD_FILE, t=3, framerate=24, loop=1).output(TITLE_CARD_VIDEO).run()
            v_files.insert(0, ffmpeg.input(TITLE_CARD_VIDEO))
    except ffmpeg.Error as e:
        print(e.stderr)
    try:
        joined_video = ffmpeg.concat(*v_files, v=1, unsafe=True)
        out, err = ffmpeg.output(joined_video[1], './output.mp4').run(capture_stderr=True)
    except ffmpeg.Error as e:
        print(e.stderr)

os.remove('./title.mp4')
clear_clean_clips()
combine_clips()