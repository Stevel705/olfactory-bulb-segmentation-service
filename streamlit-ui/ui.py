import io

import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder

import streamlit as st

# FastAPI endpoint
backend = "http://segmentation-server:8000/segmentation"


def process(image, server_url: str):

    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r


st.title("Olfactory bulb segmentation")

st.write(
    """Obtain semantic segmentation maps of the image in input via U-Net implemented in PyTorch.
        Visit this URL at `:8000/docs` for swagger documentation."""
)

input_image = st.file_uploader("Insert image")

if st.button("Make a mask prediction"):

    original, prediction = st.columns(2)

    if input_image:
        segments = process(input_image, backend)
        original_image = Image.open(input_image).convert("RGB")
        prediction_image = Image.open(
            io.BytesIO(segments.content)).convert("RGB")
        original.header("Original")
        original.image(original_image, use_column_width=True)
        prediction.header("Prediction")
        prediction.image(prediction_image, use_column_width=True)

    else:
        st.write("Insert an image!")
