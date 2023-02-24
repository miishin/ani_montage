from PIL import Image, ImageDraw, ImageFont
from os import remove, path

DEFAULT_DIMENSIONS = (854, 480)
EVA_FONT = "./EVA-Matisse_Classic.ttf"
BEBOP_FONT = "./Cheltenham Condensed Bold Italic.ttf"
OUTPUT_IMAGE = "./title.png"

def generate_blank_title_card(width, height):
    img = Image.new("RGB", (width, height), 0)
    return (img, ImageDraw.Draw(img))

def generate_eva_card(width, height, lines):
    image, draw = generate_blank_title_card(width, height)
    font_sizes = [height // 6, height // 6, height // 5, height // 10, height // 8]
    fonts = [ImageFont.truetype(font=EVA_FONT, size=s) for s in font_sizes]

    x = y = font_sizes[0] // 2
    for n in range(len(lines)):
        print(n)
        draw.text((x, y), lines[n], fill="white", font=fonts[n])
        y += font_sizes[n]
    image.save(OUTPUT_IMAGE)

def generate_bebop_card(width, height, text):
    image, draw = generate_blank_title_card(width, height)
    font_size = height // 14
    font = ImageFont.truetype(font=BEBOP_FONT, size=font_size)
    bounding = font.getbbox(text)
    draw.text((width - bounding[2] - bounding[3], height - 3.5 * bounding[3]), text, fill='white', font=font)
    image.save(OUTPUT_IMAGE)

def generate_my_bebop_card(width, height, username):
    generate_bebop_card(width, height, "%s HAS A GOOD EYE..." % username.upper())

def generate_my_eva_card(width, height, username):
    generate_eva_card(width, height, ["YOUR", "ANILIST", "FAVORITES", "USER:", username.upper()])

def main(username, tc):
    if path.isfile(OUTPUT_IMAGE):
        remove(OUTPUT_IMAGE)
    mapping = {"bebop": generate_my_bebop_card, "eva": generate_my_eva_card}
    if tc in mapping:
        mapping[tc](*DEFAULT_DIMENSIONS, username)
    else:
        generate_my_bebop_card(*DEFAULT_DIMENSIONS, username)