FROM python:3.8

WORKDIR /flask-app-dev

COPY . /flask-app-dev

RUN pip install -r requirements.txt

CMD ["python", "./start.py"]