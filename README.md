# Repository name: Spark_streaming_project_public
# Author name: Pawonrat Khumngoen

      Currently, I’m primarily working with batch processing systems, but I’ve been actively exploring and developing an interest in real-time streaming data processing. To challenge myself and expand my skill set, I initiated a real-time streaming project. 
      In this project, I utilized tools and languages such as Docker, Spark, PySpark, and Python. Since I didn’t have access to a real-time data source, I decided to implement Apache Kafka as a message broker to simulate streaming data.

### This project has 3 parts.
#### First, Kafka Producer:
1. I developed and debugged a Python script (Kafka_producer.py) to send simulated financial transaction messages to a Kafka topic named 'financial_transaction_topic'.
2. Each message was mocked and serialized in JSON format, following a predefined schema as shown below.
     </br> </br> <img width="429" height="372" alt="image" src="https://github.com/user-attachments/assets/80551a86-dee8-4393-b831-8b907dadb1a2" />
     </br>
3. The Kafka Producer continuously generates and sends transactions at 2-second intervals. It runs infinitely until manually interrupted by keyboard interrupt on the terminal, or a Kafka crash or shutdown itself.
4. As this project focuses on simulating real-time streaming rather than performance optimization, advanced Kafka configurations such as partitioning and replication are not applied. Thus, A single Kafka broker is sufficient for this project.

#### Second, Kafka Consumer:
1. I developed and debugged a Python script (Kafka_consumer.py) to consume and manually commit financial transaction messages from a Kafka Producer, which has a topic named 'financial_transaction_topic'.

#### Third, Streaming with Spark:
1. I developed and debugged a Jupyter Notebook (KafkaStreaming.ipynb) to read data from the Kafka topic.
2. Since the data is streamed in real-time and continuously flows from Kafka Producer, I implemented logic to do batch processing and export it as Parquet files for downstream processing.
