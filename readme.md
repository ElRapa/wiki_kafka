# Collect changes on Wikipedia and save to Kafka using Python
This code was written to collect all changes made to every wikipedia-domains. The changes are streamed via "https://stream.wikimedia.org/v2/stream/recentchange". Stream is extracted using pythons-sseclient-library and saved to three Kafka-Broker in a docker-container (zookeeper + confluentinc/cp-kafka). Topics on Kafka-Broker are read using Kafka-Python-library and aggregated and saved to csv using python.

# General steps:
#### 1. clone repository
#### 2. generate kafka-docker container with 3 brokers
#### 3. Create and run python-docker image for kafka-producer streaming wiki-changes and saving as Kafka-Topics
#### 4. Run 2nd python-docker image for kafka-consumer reading Kafka-Topic, analyse content and save to csv


## To run code enter following codes in command line

### Clone git-Repo and go to dir
> git clone https://github.com/ElRapa/wiki_kafka.git<br />
> cd wiki_kafka

### Run kafka via docker-compose (Note: docker doesn't mount local drive. For mounting unhash docker-compose.yml)
> docker-compose up -d

### Create python docker-image
> docker build -t python-kafka .

### create python-docker and run producer.py
> docker run -it --rm --network=host python_kafka python producer.py -h

### open another terminal and type following to create python-docker and run consumer.py
> docker run -it --rm --network=host python_kafka python consumer.py -h


End with "ctrl+c"
