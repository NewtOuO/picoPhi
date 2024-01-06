"""
Author: Newt
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np


class TextPixelator:
    def __init__(self, pixel_size: tuple, font_size: int, font_type: str) -> None:
        self._pixel_width, self._pixel_height = pixel_size
        self._font_size = font_size
        self._font_type = font_type

    def text_px(
        self,
        text: str,
        offset: tuple = (0, 0),
        pattern: tuple = (255, 255, 255),
        background: tuple = (0, 0, 0),
    ):
        pixel = Image.new(
            "RGB", (self._pixel_width, self._pixel_height), color=background
        )
        draw = ImageDraw.Draw(pixel)
        config = ImageFont.truetype(self._font_type, self._font_size)
        xy = offset
        draw.text(xy=xy, text=text, fill=pattern, font=config)
        matrix = np.array(list(pixel.getdata())).reshape(
            (self._pixel_height, self._pixel_width, 3)
        )
        return matrix


class ImagePixelator:
    def __init__(self, pixel_size: tuple) -> None:
        self._pixel_width, self._pixel_height = pixel_size

    def image_px(self, image: str) -> list:
        with Image.open(image).convert("RGB") as raw_image:
            pixel = raw_image.resize(
                (self._pixel_width, self._pixel_height),
                resample=Image.NEAREST,
            )
            matrix = np.array(list(pixel.getdata())).reshape(
                (self._pixel_height, self._pixel_width, 3)
            )
        return matrix
