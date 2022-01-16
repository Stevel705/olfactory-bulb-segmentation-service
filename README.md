# Segmentation of olfactory bulbs with web interface


When developing APIs that are designed for machine learning models, it may be convenient to have a backend and a user interface in order to conveniently experiment with machine learning models.


As a result, we have developed a service which does semantic segmentation of the olfactory bulb using [FastAPI](https://fastapi.tiangolo.com/) as the backend, and the [streamlit](https://streamlit.io/) library as the UI.

We use docker-compose to connect these two services.

To run the example on a computer that has [Docker](https://www.docker.com/) and docker-compose installed, run:
    
    docker-compose up --build
    

To view a brief documentation on the resulting API of the service, visit http://localhost:8000/docs using a web browser. 

To visit the streamlit UI, visit http://localhost:8001.

As a test image, you can use the file 'raw_1.tif' in the folder `segmentation-server/binary_segmentation/test/`


Logs can be checked using:

    docker-compose logs

