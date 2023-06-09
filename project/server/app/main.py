from fastapi import FastAPI, File, UploadFile
from fastapi.responses import ORJSONResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse

import cv2

import datetime

import processer

now = datetime.datetime.now()
today = now.strftime('%M%S%f')

app = FastAPI()

processer = processer.processer(today)


@app.get("/upload_add_line")
async def get_process_data(name: str,vert: int,hori: int,title: str):
    # 画像を読み込む
    processer.read_img(name)

    img = processer.process_line(vert,hori)
    img = processer.write_title(title)

    cv2.imwrite(today + ".jpg", img)
    return {"message": "加工が完了しました。"}

@app.get("/download_processed")
async def download_processed():
    # 加工済みの画像を読み込む
    with open(today + ".jpg", "rb") as file:
        contents = file.read()

    # ダウンロードするためのレスポンスを作成する
    response = StreamingResponse(iter([contents]), media_type="image/jpeg")
    response.headers["Content-Disposition"] = "attachment; filename="+ today + ".jpg"

    return response
