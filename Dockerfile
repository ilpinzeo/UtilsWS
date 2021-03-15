FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install Django image
COPY . /code/
#CMD django-admin startproject webserver .
CMD python manage.py runserver 0.0.0.0:8000