from PIL import Image, ImageDraw, ImageFont

DEFAULT_DIMENSIONS = (854, 480)
EVA_FONT = "./EVA-Matisse_Classic.ttf"
BEBOP_FONT = "./Cheltenham Condensed Bold Italic.ttf"

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
    image.save("./title.png")

def generate_bebop_card(width, height, text):
    image, draw = generate_blank_title_card(width, height)
    font_size = height // 14
    font = ImageFont.truetype(font=BEBOP_FONT, size=font_size)
    bounding = font.getbbox(text)
    draw.text((width - bounding[2] - bounding[3], height - 3.5 * bounding[3]), text, fill='white', font=font)
    image.save("./title.png")

def generate_bebop_card_temp(width, height, username):
    generate_bebop_card(width, height, "%s HAS A GOOD EYE..." % username.upper())

def generate_eva_card_temp(width, height, username):
    lines = ["YOUR", "ANILIST", "FAVORITES", "USER:", username.upper()]
    generate_eva_card(width, height, lines)

generate_bebop_card_temp(*DEFAULT_DIMENSIONS, "miishin")
#generate_eva_card_temp(*DEFAULT_DIMENSIONS, "miishin")
