from fastapi import FastAPI, File, UploadFile

import NumberOperations
import AfterAuth
import JPGFileOperations

app = FastAPI()

@app.get("/")
async def StartMain():
    return 'Filip Mystek'


@app.get("/auth/{creditnails}")
async def AuthWithTime(login: str, password:str ):
     return {'time': AfterAuth.returnActualTime(login,password)}

@app.get("/number/{item_id}")
async def Number(item_id: int):
     return {item_id : NumberOperations.IsNumberPrime(item_id)}


@app.post("/ImageColorInvert")
def image_filter(img: UploadFile = File(...)):
     return JPGFileOperations.invertImageColors(img)
#
