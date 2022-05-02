FROM python:3.9.5-slim-buster

COPY . /app/

RUN pip install --no-cache-dir --disable-pip-version-check -r /app/requirements.txt

WORKDIR /app/

