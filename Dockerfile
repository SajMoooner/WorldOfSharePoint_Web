FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY requirements.txt /app/requirments.txt
RUN pip install -r requirements.txt
COPY . /app
