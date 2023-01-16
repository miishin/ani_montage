import ffmpeg
import os

CLIP_DIRECTORY = "./clips/"
CLIP_FILES = os.listdir(CLIP_DIRECTORY)

def open_files():
    return [ffmpeg.input(CLIP_DIRECTORY + file) for file in CLIP_FILES]

#unfinished
def sanitize_clips():
    for file in CLIP_FILES:
        (
            ffmpeg.input(os.path.join(CLIP_DIRECTORY, file))
            .filter("s")
        )

def combine_clips():
    va_files = [item for sublist in map(lambda f: [f.video, f.audio], open_files()) for item in sublist]
    joined_video = ffmpeg.concat(*va_files, v=1, a=1).node
    ffmpeg.output(joined_video[0], joined_video[1], 'output.mp4').run()
