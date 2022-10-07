FROM python:3.10-slim as my_app_base

RUN apt-get update && apt-get -y install libpq-dev gcc

RUN python3 -m pip install --upgrade pip && pip install psycopg2

FROM my_app_base

WORKDIR /stg_wtb

ADD requirements.txt .

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

ADD . .
