# pull official base image
FROM python:3.10-bullseye

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
