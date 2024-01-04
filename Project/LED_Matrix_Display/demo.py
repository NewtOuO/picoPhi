import ws2812b
import pixelation
import time


def main() -> None:
    width, height = (16, 16)
    led = ws2812b.PixelRgb((width, height))
    pixel = pixelation.ImagePixelator((width, height))
    for _ in range(10):
        matrix = pixel.image("sprite_0.png")
        led.draw_matrix(matrix, 0, 0)
        led.display()
        time.sleep(0.5)
        matrix = pixel.image("sprite_1.png")
        led.draw_matrix(matrix, 0, 0)
        led.display()
        time.sleep(0.5)
        matrix = pixel.image("sprite_2.png")
        led.draw_matrix(matrix, 0, 0)
        led.display()
        time.sleep(0.5)
        matrix = pixel.image("sprite_3.png")
        led.draw_matrix(matrix, 0, 0)
        led.display()
        time.sleep(0.5)
    led.clear_matrix()
    led.display()


if __name__ == "__main__":
    main()
