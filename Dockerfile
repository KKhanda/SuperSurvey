FROM python:3.5.4
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 CMD python supersurvey/manage.py runserver 0.0.0.0:8000