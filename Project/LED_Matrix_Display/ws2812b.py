"""
Author: Newt
"""
import board
import neopixel

class Strip:
    def __init__(self, count: int, pin: board = board.D10) -> None:
        self.led = neopixel.NeoPixel(pin=pin, n=count, brightness=1, auto_write=False)

    def _check_rgb_value_range(self, rgb: tuple) -> None:
        if not all(0 <= value <= 15 for value in rgb):
            raise ValueError("RGB values must be between 0 and 15 (1-bits RGB)")

    def set_led(self, indices: list, rgb: tuple) -> None:
        self._check_rgb_value_range(rgb)
        for index in indices:
            self.led[index] = rgb

    def fill_led(self, rgb: tuple) -> None:
        self._check_rgb_value_range(rgb)
        self.led.fill(rgb)

    def display(self):
        self.led.show()


class PixelRgb:
    def __init__(self, pixel_size: tuple, pin: board = board.D10) -> None:
        self.pixel = []
        self.pixel_width, self.pixel_height = pixel_size
        for _ in range(self.pixel_height):
            self.pixel.append([(0, 0, 0)] * self.pixel_width)
        self.led = neopixel.NeoPixel(
            pin=pin,
            n=self.pixel_width * self.pixel_height,
            brightness=1,
            auto_write=False,
        )

    def _check_matrix(self, matrix) -> None:
        for row in matrix:
            for item in row:
                if type(item) != tuple:
                    raise ValueError(f"Matrix must be tuple")
                self._check_rgb_value_range(item)

    def _check_rgb_value_range(self, rgb: tuple) -> None:
        if not all(0 <= value <= 15 for value in rgb):
            raise ValueError("RGB values must be between 0 and 15 (1-bits RGB)")

    def _format_matrix(self, matrix: list) -> list:
        formatted_matrix = []
        for index, row in enumerate(matrix):
            if index % 2 == 0:
                formatted_matrix.append(list(reversed(row)))
            else:
                formatted_matrix.append(row)
        return formatted_matrix

    def draw_matrix(self, matrix: list, x: int, y: int) -> None:
        self._check_matrix(matrix)
        for index, row in enumerate(matrix):
            self.pixel[y + index][x : x + len(row)] = row

    def clear_matrix(self) -> None:
        self.pixel = [[(0, 0, 0) for _ in row] for row in self.pixel]

    def display(self):
        formatted_matrix = self._format_matrix(self.pixel)
        for row_index, row in enumerate(formatted_matrix):
            for index, item in enumerate(row):
                self.led[row_index * self.pixel_width + index] = item
        self.led.show()


class PixelMonochrome:
    def __init__(self, pixel_size: tuple, pin: board = board.D10) -> None:
        self.pixel = []
        self.pixel_width, self.pixel_height = pixel_size
        for _ in range(self.pixel_height):
            self.pixel.append([0] * self.pixel_width)
        self.led = neopixel.NeoPixel(
            pin=pin,
            n=self.pixel_width * self.pixel_height,
            brightness=1,
            auto_write=False,
        )

    def _check_matrix(self, matrix) -> None:
        for row in matrix:
            for item in row:
                if type(item) != int or (item != 0 and item != 1):
                    raise ValueError(f"Matrix must be 0 or 1")

    def _check_rgb_value_range(self, rgb: tuple) -> None:
        if not all(0 <= value <= 15 for value in rgb):
            raise ValueError("RGB values must be between 0 and 15 (2-bits RGB)")

    def _format_matrix(self, matrix: list) -> list:
        formatted_matrix = []
        for index, row in enumerate(matrix):
            if index % 2 == 0:
                formatted_matrix.append(list(reversed(row)))
            else:
                formatted_matrix.append(row)
        return formatted_matrix

    def draw_matrix(self, matrix: list, x: int, y: int) -> None:
        self._check_matrix(matrix)
        for index, row in enumerate(matrix):
            self.pixel[y + index][x : x + len(row)] = row

    def clear_matrix(self) -> None:
        self.pixel = [[0 for _ in row] for row in self.pixel]

    def display(self, pattern: tuple = (1, 1, 1), background: tuple = (0, 0, 0)):
        self._check_rgb_value_range(pattern)
        self._check_rgb_value_range(background)
        formatted_matrix = self._format_matrix(self.pixel)
        for row_index, row in enumerate(formatted_matrix):
            for index, item in enumerate(row):
                if item == 1:
                    self.led[row_index * self.pixel_width + index] = pattern
                else:
                    self.led[row_index * self.pixel_width + index] = background
        self.led.show()
