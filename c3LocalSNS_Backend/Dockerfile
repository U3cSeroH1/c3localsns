FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
ADD Pipfile /web/
ADD Pipfile.lock /web/
RUN pip install pipenv && pipenv install