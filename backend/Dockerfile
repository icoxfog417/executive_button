FROM python:3.7

# set work directory
WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y python3-dev libpq-dev unixodbc-dev

# install dependencies
RUN pip install --upgrade pip setuptools
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /backend/
RUN chomd 755 backend/script/run.sh
