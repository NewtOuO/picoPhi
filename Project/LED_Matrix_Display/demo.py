from led_strip import WS2812B
from pixelation import Pixelator
from time import sleep


led_width = 16
led_height = 16


def format_matrix(matrix) -> list:
    """Due to the S-shaped arrangement of the WS2812B, the array needs to be reversed in odd rows."""
    text_index = []
    for row, values in enumerate(matrix):
        if row % 2 == 0:
            values = reversed(values)
        text_index.extend(
            [
                row * led_width + index
                for index, value in enumerate(values)
                if value == 1
            ]
        )
    return text_index


def show_text(pixel: Pixelator, led: WS2812B) -> None:
    led.fill((0, 0, 0))
    matrix = format_matrix(
        pixel.pixelate_text(
            text="完", font_type="NotoSansTC.ttf", offset=(0, -5), font_size=14
        )
    )
    led.set_led(matrix, (3, 0, 0))
    led.show()
    sleep(1)
    led.fill((0, 0, 0))
    matrix = format_matrix(
        pixel.pixelate_text(
            text="成", font_type="NotoSansTC.ttf", offset=(0, -5), font_size=14
        )
    )
    led.set_led(matrix, (3, 0, 0))
    led.show()
    sleep(1)
    led.fill((0, 0, 0))
    matrix = format_matrix(
        pixel.pixelate_text(
            text="了", font_type="NotoSansTC.ttf", offset=(0, -5), font_size=14
        )
    )
    led.set_led(matrix, (3, 0, 0))
    led.show()
    sleep(1)
    led.fill((0, 0, 0))


def main() -> None:
    pixel = Pixelator(led_width, led_height)
    led = WS2812B(count=led_width * led_height)
    show_text(pixel, led)


if __name__ == "__main__":
    main()
