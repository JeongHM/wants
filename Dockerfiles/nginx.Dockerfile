FROM nginx:1.18.0

WORKDIR /home

COPY ./nginx .

EXPOSE 80
