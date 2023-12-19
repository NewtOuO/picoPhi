from PIL import Image, ImageDraw, ImageFont
import board
import neopixel
import time

LENGTH = 256
FONT_SIZE = 14.5
PIXEL_BRIGHTNESS = 0.02

pixels = neopixel.NeoPixel(
    board.D10, LENGTH, brightness=PIXEL_BRIGHTNESS, auto_write=False
)


def text_to_matrix(text, font_size=FONT_SIZE):
    image = Image.new("1", (16, 16), color=1)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Cubic.ttf", font_size)
    draw.text((0, 0), text, font=font, fill=0)
    matrix = list(image.getdata())
    matrix = [matrix[i : i + 16] for i in range(0, len(matrix), 16)]
    return matrix


def display_text_on_pixels(text):
    for char in text:
        matrix = text_to_matrix(char)
        for index, row in enumerate(matrix, start=1):
            row = row[::-1] if index % 2 != 0 else row
            for key, pixel_value in enumerate(row):
                pixel_value = 1 - pixel_value
                pixels[(16 * (index - 1)) + key] = (
                    pixel_value * 128,
                    pixel_value * 128,
                    pixel_value * 128,
                )
        pixels.show()
        time.sleep(0.5)


chinese_text = "信澄想明毅了"
while True:
    display_text_on_pixels(chinese_text)
