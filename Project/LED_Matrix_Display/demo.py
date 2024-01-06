"""
Author: Newt
"""
from ws2812b import PixelRGB, PixelBool
from pixelation import ImagePixelator, TextPixelator
import time


def main() -> None:
    img = ImagePixelator((16, 16))
    txt = TextPixelator((32, 16), 12, "NotoSansTC.ttf")

    pxrgb = PixelRGB((16, 16))
    img0 = img.image_px("img_0.png")
    img1 = img.image_px("img_1.png")
    img2 = img.image_px("img_2.png")

    pxbool = PixelBool((16, 16))
    txt = txt.text_px("Newt")

    # Demo 1
    for a in range(-15, 16):
        pxrgb.draw(img0, (0, a))
        pxrgb.display()
        pxrgb.clear()
        time.sleep(0.05)
    pxrgb.display()

    # Demo 2
    for b in range(-32, 16):
        pxbool.draw(txt, (b, 0))
        pxbool.display((32, 32, 0), (0, 0, 16))
        pxbool.clear()
        time.sleep(0.05)
    pxbool.display((0, 0, 0), (0, 0, 0))

    # Demo 3
    for c in range(5):
        pxrgb.draw(img0, (0, 0))
        pxrgb.display()
        pxrgb.clear()
        time.sleep(0.2)
        pxrgb.draw(img1, (0, 0))
        pxrgb.display()
        pxrgb.clear()
        time.sleep(0.2)
        pxrgb.draw(img0, (0, 0))
        pxrgb.display()
        pxrgb.clear()
        time.sleep(0.2)
        pxrgb.draw(img2, (0, 0))
        pxrgb.display()
        pxrgb.clear()
        time.sleep(0.2)
    pxrgb.display()


if __name__ == "__main__":
    main()
