"""
Author: Newt
"""
from PIL import Image, ImageDraw, ImageFont


class TextPixelator:
    def __init__(self, pixel_size: tuple, font_size: int, font_type: str) -> None:
        self.pixel_width, self.pixel_height = pixel_size
        self.font_size = font_size
        self.font_type = font_type

    def text(
        self, text: str, offset_x: int = 0, offset_y: int = 0, center: bool = False
    ):
        matrix = []
        pixel = Image.new("1", (self.pixel_width, self.pixel_height), color=0)
        draw = ImageDraw.Draw(pixel)
        config = ImageFont.truetype(self.font_type, self.font_size)
        xy = (offset_x, offset_y)
        if center:
            left, top, right, bottom = config.getbbox(text)
            xy = (
                (self.pixel_width - (right - left)) // 2 + offset_x,
                (self.pixel_height - (bottom - top)) // 2 + offset_y,
            )
        draw.text(
            xy=xy,
            text=text,
            fill=1,
            font=config,
        )

        for row in range(0, self.pixel_width * self.pixel_height, self.pixel_width):
            matrix.append(list(pixel.getdata())[row : row + self.pixel_width])

        return matrix


class ImagePixelator:
    def __init__(self, pixel_size: tuple) -> None:
        self.pixel_width, self.pixel_height = pixel_size

    def _compress_color(self, color_value: int) -> int:
        return int(color_value // 16)

    def image(self, image: str) -> list:
        matrix = []
        with Image.open(image).convert("RGB") as raw_image:
            pixel = raw_image.resize(
                (self.pixel_width, self.pixel_height),
                resample=Image.NEAREST,
            )
        for row in range(0, self.pixel_width * self.pixel_height, self.pixel_width):
            row_rgb = list(pixel.getdata())[row : row + self.pixel_width]
            compressed_row_rgb = [
                tuple(map(self._compress_color, rgb)) for rgb in row_rgb
            ]
            matrix.append(compressed_row_rgb)
        return matrix
