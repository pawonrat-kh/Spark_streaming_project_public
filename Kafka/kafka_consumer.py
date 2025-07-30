import json
import logging
from kafka import KafkaConsumer
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FinanceTransactionConsumer:
    def __init__(self, bootstrap_servers = os.environ['BOOTSTRAP_SERVERS'], topic = os.environ['TOPICS_NAME'], group_id = os.environ['CONSUMER_GROUP_ID']):
        self.topic = topic
        self.group_id = group_id
        
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers = bootstrap_servers,
            group_id = group_id,
            value_deserializer = lambda x: json.loads(x.decode('utf-8')),
            key_deserializer = lambda x: x.decode('utf-8') if x else None,
            enable_auto_commit = False # Do at exactly once processsing
        )
        
        self.message_count = 0
    
    def consume_transactions(self):
        """Main consumption loop"""
        logger.info(f"Starting consumer for topic: {self.topic}")
        logger.info(f"Group ID: {self.group_id}")
        
        try:
            for message in self.consumer:
                # Process the transaction
                if message:
                    self.message_count += 1
                    logger.info(f"Processed transaction {self.message_count}: "
                              f"{message.value['transaction_id'][:8]}... - "
                              f"{message.value['transaction_type']} - "
                              f"${message.value['amount']} - "
                              f"${message.value['currency_rate']}")
                self.consumer.commit()
                    
        except Exception as e:
            logger.error(f"Consumer error: {e}")
        finally:
            self.consumer.close()

if __name__ == "__main__":

    consumer = FinanceTransactionConsumer(
        bootstrap_servers = os.environ['BOOTSTRAP_SERVERS'],
        topic = os.environ['TOPICS_NAME'],
        group_id = os.environ['CONSUMER_GROUP_ID']
    )
    
    consumer.consume_transactions()
