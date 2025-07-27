# Repository name: Spark_streaming_project_public
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
1. Once Kafka_producer.py is executed, the terminal outputs logs related to currency rate fetching. For each message, a currency is randomly selected from the schema defined in schema.py, and the message details are then displayed accordingly.
   <img width="1513" height="769" alt="Kafka_producer" src="https://github.com/user-attachments/assets/509f93d3-ee7d-4245-9838-535670b31632" />
#### Kafka Consumer part:
1. Once Kafka_consumer.py is executed, the terminal logs the consumption of messages from the Kafka topic 'financial_transaction_topic'.
   <img width="1481" height="738" alt="image" src="https://github.com/user-attachments/assets/5f3f9c5a-255a-45bc-bb28-63199d64ed9d" />
#### Streaming with Spark part:
1. To test Kafka accessibility and perform basic analysis, I executed the cell to display the number of transactions grouped by currency.
   <img width="271" height="173" alt="image" src="https://github.com/user-attachments/assets/8a204409-55eb-4eca-adff-86cf8c6c60d6" />

---------------------------------------------------------------------------------------------

#### Setting environment
1. For the Docker-Compose file, I obtained and modified it from the initial Confluent GitHub repository (https://github.com/confluentinc/cp-all-in-one/blob/8.0.0-post/cp-all-in-one/docker-compose.yml)
2. I added a Dockerfile to be able lauch Jupyter notebook on Spark

   
