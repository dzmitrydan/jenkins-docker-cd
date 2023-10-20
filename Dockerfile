FROM python:3.8

WORKDIR /flask-app

COPY . /flask-app

RUN pip install -r requirements.txt

CMD ["python", "./start.py"]