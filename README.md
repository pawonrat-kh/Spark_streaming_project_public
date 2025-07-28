# Repository name: real_time_stream_processing_project_public
# Project name: Real-time Stream processing data pipeline with Apache Kafka and Apache Spark
# Author name: Pawonrat Khumngoen

      Currently, I’m primarily working with batch processing systems, but I’ve been actively exploring and developing an interest in real-time streaming data processing. To challenge myself and expand my skill set, I initiated a real-time streaming project. 
      In this project, I utilized tools and languages such as Docker, Spark, PySpark, and Python. Since I didn’t have access to a real-time data source, I decided to implement Apache Kafka as a message broker to simulate streaming data.

### The project has 3 parts.
#### First, Kafka Producer:
1. I developed and debugged a Python script (Kafka_producer.py) to send simulated financial transaction messages to a Kafka topic named 'financial_transaction_topic'.
2. Each message was mocked and serialized in JSON format, following a predefined schema as shown below.
     </br> </br> <img width="429" height="372" alt="image" src="https://github.com/user-attachments/assets/80551a86-dee8-4393-b831-8b907dadb1a2" />
     </br>
3. The Kafka Producer continuously generates and sends transactions at 2-second intervals. It runs infinitely until manually interrupted by a keyboard interrupt on the terminal, or a Kafka crash or shutdown.
4. As this project focuses on simulating real-time streaming rather than performance optimization, advanced Kafka configurations such as partitioning and replication are not applied. Thus, A single Kafka broker is sufficient for this project.

#### Second, Kafka Consumer:
1. I developed and debugged a Python script (Kafka_consumer.py) to consume and manually commit financial transaction messages from a Kafka Producer.

#### Third, Streaming with Spark:
1. I developed and debugged a Jupyter Notebook (KafkaStreaming.ipynb) to read data from the Kafka topic.
2. Since the data is streamed in real-time and continuously flows from Kafka Producer, I implemented logic to do batch processing and export it as Parquet files for downstream processing at a destination path.

---------------------------------------------------------------------------------------------

### The results.
#### Kafka Producer part:
* Once Kafka_producer.py is executed, the terminal outputs logs related to currency rate fetching via a REST API. For each message, a currency is randomly selected from the schema defined in schema.py, and the message details are displayed.</br></br>
   <img width="1513" height="769" alt="Kafka_producer" src="https://github.com/user-attachments/assets/509f93d3-ee7d-4245-9838-535670b31632" /></br>
#### Kafka Consumer part:
* Once Kafka_consumer.py is executed, the terminal displays logs showing the messages being consumed by the Kafka consumer from the topic 'financial_transaction_topic'.</br></br>
   <img width="1481" height="738" alt="Kafka_consumer" src="https://github.com/user-attachments/assets/2801fc15-766f-40a7-a31c-714bed6195a2" /></br>
#### Streaming with Spark part:
* To verify Kafka connectivity and demonstrate basic analytical capability, I ran a sample query to display the number of transactions grouped by currency.</br></br>
   <img width="271" height="173" alt="image" src="https://github.com/user-attachments/assets/8a204409-55eb-4eca-adff-86cf8c6c60d6" /></br>

---------------------------------------------------------------------------------------------

#### Setting environment.
1. Based on the initial Docker Compose setup from the Confluent GitHub repository (https://github.com/confluentinc/cp-all-in-one/blob/8.0.0-post/cp-all-in-one/docker-compose.yml), I obtained and modified this docker-compose.yml file to suit the project’s requirements.
2. Added a custom Dockerfile to enable launching a Jupyter Notebook with Apache Spark support.
3. Created a requirements.txt file to specify Python dependencies, ensuring the environment runs consistently within a virtual environment.

---------------------------------------------------------------------------------------------

#### Skill sets.
1. Apache Kafka.
2. Kafka Producer API.
3. Kafka Consumer API.
4. Apache Spark.
5. Python.
6. PySpark.
7. Docker.
8. Jupyter Notebook.
9. Real-time Stream Processing.
10. Batch Processing.
11. Message Queuing.
12. Data pipeline.
13. REST API

