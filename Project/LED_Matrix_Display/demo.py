"""
Author: Newt
"""
from ws2812b import Pixel
from pixelation import ImagePixelator, TextPixelator
from time import sleep

pxsize = (16, 16)
px = Pixel(pxsize)

img_pxr = ImagePixelator(pxsize)
img0 = img_pxr.image_px("img_0.png")
img1 = img_pxr.image_px("img_1.png")
img2 = img_pxr.image_px("img_2.png")

txt_pxr = TextPixelator((32, 16), 12, "NotoSansTC.ttf")
txt = txt_pxr.text_px("Newt")


def demo_1() -> None:
    for y in range(-16, 16):
        px.draw(img0, (0, y))
        px.display()
        px.clear()
    px.display()


def demo_2() -> None:
    for x in range(-16, 16):
        px.draw(txt, (x, 0))
        px.display()
        px.clear()
    px.display()


def demo_3() -> None:
    for _ in range(3):
        px.draw(img0, (0, 0))
        px.display()
        px.clear()
        sleep(0.2)
        px.draw(img1, (0, 0))
        px.display()
        px.clear()
        sleep(0.2)
        px.draw(img0, (0, 0))
        px.display()
        px.clear()
        sleep(0.2)
        px.draw(img2, (0, 0))
        px.display()
        px.clear()
        sleep(0.2)
    px.display()


def demo_4() -> None:
    for _ in range(3):
        for x in range(-20, 20):
            px.draw(img0)
            px.draw(txt, (x, 0))
            px.display()
            px.clear()
    px.display()


def main() -> None:
    demo_1()
    demo_2()
    demo_3()
    demo_4()


if __name__ == "__main__":
    main()
