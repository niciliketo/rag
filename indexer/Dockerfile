FROM python:3.10-slim
WORKDIR /app
# Do this first to prevent rebuilding every time...
COPY requirements.txt /app/requirements.txt
# These libraries seem to be needed to index content (possibly from pdfs)
# RUN apt-get update && apt-get install libgl1 -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt
#RUN mkdir -p /app/data
ADD . /app
#ADD ./data /app/data
