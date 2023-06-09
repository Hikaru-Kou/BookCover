import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont


class writer_function():
    def __init__(self) -> None:
          pass
    def cv2_putText_1(img, text, org, fontFace, fontScale, color):
        x, y = org
        b, g, r = color
        colorRGB = (r, g, b)
        imgPIL = cv2pil(img)
        draw = ImageDraw.Draw(imgPIL)
        fontPIL = ImageFont.truetype(font = fontFace, size = fontScale)
        draw.text(xy = (x,y), text = text, fill = colorRGB, font = fontPIL)

        imgCV = pil2cv(imgPIL)
        return imgCV


def pil2cv(imgPIL):
        imgCV_RGB = np.array(imgPIL, dtype = np.uint8)
        imgCV_BGR = np.array(imgPIL)[:, :, ::-1]
        return imgCV_BGR

def cv2pil(imgCV):
        imgCV_RGB = imgCV[:, :, ::-1]
        imgPIL = Image.fromarray(imgCV_RGB)
        return imgPIL
