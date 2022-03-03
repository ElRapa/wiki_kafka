# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# CMD ["python", "producer.py"]
# CMD ["python", "test.py"]
# docker run -it --rm --network=host python_kafka python producer.py -h