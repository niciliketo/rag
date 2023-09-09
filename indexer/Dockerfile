FROM python:3.10-slim
WORKDIR /app
RUN mkdir -p /app/data
ADD . /app
ADD ./data /app/data
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["indexer.py"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]

