FROM python:3.7-slim

RUN mkdir /streamlit-ui

COPY requirements.txt /streamlit-ui

WORKDIR /streamlit-ui

RUN pip install -r requirements.txt

COPY . /streamlit-ui

EXPOSE 8001

CMD ["streamlit", "run", "ui.py", "--server.port", "8001"]