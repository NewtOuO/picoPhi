"""
Author: Newt
Version: 1.0
"""
import board
import neopixel


class WS2812B:
    def __init__(self, count: int, pin: board = board.D10) -> None:
        self.led = neopixel.NeoPixel(pin=pin, n=count, brightness=1, auto_write=False)

    def _check_rgb_range(self, rgb: tuple) -> None:
        if not all(0 <= value <= 15 for value in rgb):
            raise ValueError("RGB values must be between 0 and 15")

    def set(self, indices: list, rgb: tuple) -> None:
        self._check_rgb_range(rgb)
        for index in indices:
            self.led[index] = rgb

    def fill(self, rgb: tuple) -> None:
        self._check_rgb_range(rgb)
        self.led.fill(rgb)

    def show(self):
        self.led.show()
