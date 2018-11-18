
FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    gettext \
    vim

EXPOSE 8000

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY requirements_dev.txt ./
RUN pip install -r requirements_dev.txt

COPY . /usr/src/app/
