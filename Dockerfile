FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /mini_commerce
WORKDIR /mini_commerce
ADD . /mini_commerce/
RUN pip install -r requirements.txt