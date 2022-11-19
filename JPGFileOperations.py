
from fastapi.responses import StreamingResponse
from io import BytesIO

import PIL
from PIL import ImageOps, Image


def invertImageColors(img: bytes):
    original_image = Image.open(img.file)
    original_image = PIL.ImageOps.invert(original_image)
    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/jpeg")
