FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir /segmentation-server

COPY requirements.txt /segmentation-server

WORKDIR /segmentation-server

RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . /segmentation-server

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]