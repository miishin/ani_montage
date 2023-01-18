from PIL import Image, ImageDraw, ImageFont

def generate_blank_title_card(width, height):
    background = Image.new("RGB", (width, height), 0)
    draw = ImageDraw.Draw(background)

def generate_eva_card(width, height, username):
    lines = ["YOUR", "ANILIST", "FAVORITES", "user:", username]
    font_sizes = [height/6, height/6, height/5, height/10, height/8]
    font = ImageFont.truetype(font="./EVA-Matisse_Classic.ttf", size=100)

def generate_bebop_card(width, height, username):
    line1 = "DO YOU WANT TO SEE"
    line2 = "%s'S FAVORITES?" % username
    font_size = height // 14
    font = ImageFont.truetype(font="./Cheltenham Condensed Bold Italic.ttf", size=100)