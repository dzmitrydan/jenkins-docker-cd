FROM python:3.8

WORKDIR /flask-app-main

COPY . /flask-app-main

RUN pip install -r requirements.txt

CMD ["python", "./start.py"]