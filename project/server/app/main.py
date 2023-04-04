from fastapi import FastAPI, File, UploadFile
from fastapi.responses import ORJSONResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse

import cv2

app = FastAPI()

@app.post("/upload_add_line")
async def upload_add_line(image: UploadFile = File(...)):
    # 画像を一時ファイルとして保存する
    with open("tmp.jpg", "wb") as buffer:
        buffer.write(await image.read())

    # 画像を読み込む
    img = cv2.imread("tmp.jpg")

    # 線を追加する
    cv2.line(img, (0, 0), (100, 100), (255, 0, 0), 5)

    # 加工した画像を保存する
    cv2.imwrite("processed.jpg", img)

    return {"message": "加工が完了しました。"}

@app.get("/download_processed")
async def download_processed():
    # 加工済みの画像を読み込む
    with open("processed.jpg", "rb") as file:
        contents = file.read()

    # ダウンロードするためのレスポンスを作成する
    response = StreamingResponse(iter([contents]), media_type="image/jpeg")
    response.headers["Content-Disposition"] = "attachment; filename=processed.jpg"

    return response
