# Enter codes in command line

# Clone git-Repo and go to dir
> git clone https://github.com/ElRapa/wiki_kafka.git
> cd wiki_kafka

# Run kafka via docker-compose
> docker-compose up -d

# Create python docker-image
docker build -t python-kafka .

# run producer in terminal
docker run -it --rm --network=host python_kafka python producer.py -h

# run consumer in another terminal
docker run -it --rm --network=host python_kafka python consumer.py -h

# end with ctrl+c