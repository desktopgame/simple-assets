from PIL import Image, ImageDraw
import style
import zipfile
import glob

#
# draw functions
#


def draw_line_rect(draw, width: int, height: int, color):
    draw.rectangle((0, 0, width, 2), fill=color)
    draw.rectangle((0, 0, 2, height), fill=color)
    draw.rectangle((0, height-3, width, height), fill=color)
    draw.rectangle((width-3, 0, width, height), fill=color)

#
# generate functions
#


def gen_image(width: int, height: int, filename: str, renderer):
    img = Image.new('RGBA', (width, height), None)
    draw = ImageDraw.Draw(img)
    renderer(draw)
    img.save(filename)


def gen_filled_rect(width: int, height: int, filename: str, color=None):
    gen_image(
        width, height,
        filename,
        lambda draw:
            draw.rectangle((0, 0, width, height), fill=color, width=1)
    )


def gen_line_rect(width: int, height: int, filename: str, color=None):
    gen_image(
        width, height,
        filename,
        lambda draw:
            draw_line_rect(draw, width, height, color)
    )


def gen_filled_circle(width: int, height: int, filename: str, color=None):
    gen_image(
        width, height,
        filename,
        lambda draw:
            draw.ellipse((0, 0, width, height), fill=color, width=1)
    )


def gen_filled_triangle(width: int, height: int, filename: str, color=None):
    gen_image(
        width, height,
        filename,
        lambda draw:
            draw.polygon([(0, height), (width/2, 0), (width, height)], fill = color)
    )


def generate(dir: str, width: int, height: int):
    styles = [
        style.Style((255, 0, 0), 'red'),
        style.Style((0, 255, 0), 'green'),
        style.Style((0, 0, 255), 'blue'),
        style.Style((235, 151, 143), 'indian_yellow'),
        style.Style((236, 223, 43), 'lemon_yellow'),
        style.Style((196, 26, 65), 'carmine_red'),
        style.Style((219, 60, 75), 'signal_red'),
        style.Style((0, 167, 113), 'emerald_green'),
        style.Style((54, 176, 131), 'cobalt_green'),
        style.Style((40, 82, 148), 'supream_blue'),
        style.Style((28, 80, 147), 'russian_blue'),
    ]
    s: style.Style
    for s in styles:
        gen_filled_rect(
            width, height,
            f'{dir}/fill_rect_{s.filename}.png', s.color)
        gen_line_rect(
            width, height,
            f'{dir}/line_rect_{s.filename}.png', s.color)
        gen_filled_circle(
            width, height,
            f'{dir}/fill_circle_{s.filename}.png', s.color)
        gen_filled_triangle(
            width, height,
            f'{dir}/fill_triangle_{s.filename}.png', s.color)


def main():
    generate('dist/32', 32, 32)
    generate('dist/64', 64, 64)
    generate('dist/96', 96, 96)
    generate('dist/128', 128, 128)
    c = zipfile.ZIP_DEFLATED
    with zipfile.ZipFile('simple-assets.zip', 'w', compression=c) as new_zip:
        files = glob.glob('dist/**/*.png', recursive=True)
        for file in files:
            print(file)
            new_zip.write(file)


if __name__ == "__main__":
    main()
