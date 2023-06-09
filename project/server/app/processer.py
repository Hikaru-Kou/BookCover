import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont


class processer():
    def __init__(self,today):
        self.today = today

    def read_img(self,name):
        img = cv2.imread(name + ".jpg")
        self.img = img

    def process_line(self,vert,hori):
        h,w=self.img.shape[:2]
        #破線の情報
        dashp=5 #破線の太さ
        dashw=10 #破線一本あたりの幅
        color=[0,0,255] #BGR三要素
        y=0 #破線の開始位置

        #破線作成開始
        i=0
        while i<w:
            self.img[int(y-dashp/2):int(y+dashp/2),i:i+dashw,:]=[0,0,255]
            i=i+dashw*2

        #線作成開始
        cv2.line(self.img,(100,0), (100, 2500), (0, 0, 0), thickness=2)
        cv2.line(self.img,(1400,0), (1400, 2500), (0, 0, 0), thickness=2)
        cv2.line(self.img,(100,100), (1600, 100), (0, 0, 0), thickness=2)
        cv2.line(self.img,(100,1600), (1600, 1600), (0, 0, 0), thickness=2)

        return self.img
    
    def write_title(self,title):
        writer_function = writer_function.writer_function()

        #img = np.full((200,400,3), (160,160,160), dtype=np.uint8)

        # 独自関数で日本語テキストを描写する
        text = title
        x, y = 200,100
        fontPIL = "fonts/DArielUnicode.ttf"
        size = 40
        colorBGR = (255,0,0) # cv2.putText()と同じく、BGRの順で定義

        self.img = writer_function.cv2_putText_1(img = self.img,
                            text = text,
                            org = (x,y),
                            fontFace = fontPIL,
                            fontScale = size,
                            color = colorBGR)