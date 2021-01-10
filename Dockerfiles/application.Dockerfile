FROM python:3.7.9-alpine3.11

WORKDIR /home

COPY . .

EXPOSE 5000

RUN pip3 install -r requirements.txt