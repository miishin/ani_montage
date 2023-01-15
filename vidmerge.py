import ffmpeg
import os

CLIP_DIRECTORY = "./clips"

#
def sanitize_clips():
    for file in os.listdir(CLIP_DIRECTORY):
        print(file)