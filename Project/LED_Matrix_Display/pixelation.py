"""
Author: Newt
"""
from PIL import Image, ImageDraw, ImageFont


class Pixelator:
    def __init__(self, pixel_width: int, pixel_height) -> None:
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height

    def pixelate_text(
        self, text: str, font_type: str, font_size: int = 14, offset: tuple = (0, 0)
    ) -> list:
        result = []
        pixel = Image.new("1", (self.pixel_width, self.pixel_height), color=0)
        draw = ImageDraw.Draw(pixel)
        config = ImageFont.truetype(font_type, font_size)
        left, top, right, bottom = config.getbbox(text)
        draw.text(
            xy=(
                (self.pixel_width - (right - left)) / 2 + offset[0],
                (self.pixel_height - (bottom - top)) / 2 + offset[1],
            ),
            text=text,
            font=config,
            fill=1,
        )
        for row in range(0, self.pixel_width * self.pixel_height, self.pixel_width):
            result.append(list(pixel.getdata())[row : row + self.pixel_width])
        return result

    def pixelate_image(self, image_path: str) -> list:
        result = []
        original_image = Image.open(image_path)
        pixel = original_image.resize(
            (
                original_image.width // self.pixel_width,
                original_image.height // self.pixel_height,
            ),
            resample=Image.NEAREST,
        )
        for row in range(0, self.pixel_width * self.pixel_height, self.pixel_width):
            result.append(list(pixel.getdata())[row : row + self.pixel_width])
        return result
