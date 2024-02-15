FROM python:3.10.7

ENV PYTHONNUNBUFFERED 1

RUN pip install psutil

WORKDIR /mysite
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8085
