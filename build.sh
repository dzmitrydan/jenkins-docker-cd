#!/bin/bash
docker build -t flask-app .
docker run -it --rm --name running-flask-app flask-app