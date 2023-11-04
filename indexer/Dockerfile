FROM python:3.10-slim
WORKDIR /app
# Do this first to prevent rebuilding every time...
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
#RUN mkdir -p /app/data
ADD . /app
#ADD ./data /app/data
