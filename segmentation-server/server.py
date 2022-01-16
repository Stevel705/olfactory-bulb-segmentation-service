import io

from binary_segmentation.predict import predict
from starlette.responses import Response

from fastapi import FastAPI, File

app = FastAPI(
    title="Olfactory bulb segmentation",
    description="""Obtain semantic segmentation mask of the image in input via U-Net implemented in PyTorch.
                Visit this URL at port 8001 for the streamlit interface.""",
    version="0.0.1",
)


@app.post("/segmentation")
def get_segmentation_mask(file: bytes = File(...)):
    """Get segmentation mask from image file
        
    - **file**: image of the olfactory bulb
        """
    segmented_image = predict(file)
    bytes_io = io.BytesIO()
    segmented_image.save(bytes_io, format="PNG")
    return Response(bytes_io.getvalue(), media_type="image/png")
