from PIL import Image, ImageDraw, ImageFont
import textwrap

# import os
# print(os.getcwd())
# im = Image.open(open('./day18_meme/salat.jpg', 'rb'))
def get_salatifikado(top_text:str, bottom_text:str, where_to_save:str):
    im = Image.open('./day18_meme/salat.jpg')

    draw = ImageDraw.Draw(im)

    image_width, image_height = im.size

    font = ImageFont.truetype(font = './fonts/impact.ttf', size = int(image_height/8))

    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width

    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)

    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)

    # im.show()
    im.save(where_to_save)

get_salatifikado('о цукерки ?!', 'ух ти', './day18_meme/memesak.png')
# pil_img.save('data/temp/lena_square_save.png')
