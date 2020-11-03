# pull official base image
FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/backend
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./Test_backend/requirements.txt .
RUN pip install -r requirements.txt
# copy entrypoint.sh
COPY ./Test_backend/entrypoint.sh /entrypoint.sh
# copy project
COPY ./Test_backend /usr/src/backend