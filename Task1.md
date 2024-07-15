```python
#Docker Creating Kafka
docker network create kafka-net

docker run -d --name zookeeper --network kafka-net -p 2181:2181 zookeeper:3.4.13

docker run -d --name kafka --network kafka-net -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 confluentinc/cp-kafka:latest

```


```python
#Create Kafka Topic Using Kafka CLI Command
docker exec -it kafka /bin/bash

[appuser@7a5cd2130dd8 ~]$kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```


```python
#Send Message to Kafka Topic Using Kafka CLI Command
[appuser@7a5cd2130dd8 ~]$ kafka-console-producer --topic test-topic --bootstrap-server localhost:9092
```


```python
#> Hello World
#> This is a Message
```


```python
#Listen to Messages Produced on Some Topic Using Kafka CLI Command(Openned new Terminal)
docker exec -it kafka /bin/bash

[appuser@7a5cd2130dd8 ~]$kafka-console-consumer --topic test-topic --bootstrap-server localhost:9092 --from-beginning
```


```python
#Hello World
#This is a Message
```
