FROM python:2.7-alpine

RUN apk add --update --no-cache build-base linux-headers pcre-dev

COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
