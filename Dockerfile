
FROM python:3.7
#FROM node:9.1

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

RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get -y install nodejs

COPY package.json package.json
RUN npm install

COPY . /usr/src/app/
