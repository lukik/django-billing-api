# pull official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install -r local.txt

# Create a directory for logs
RUN mkdir /usr/src/app/logs

# copy project
COPY . .