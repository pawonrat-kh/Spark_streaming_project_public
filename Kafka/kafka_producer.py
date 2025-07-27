import json
import random
import time
from datetime import datetime, timedelta
from kafka import KafkaProducer
from faker import Faker
import uuid
import logging
from schema import FinancialTransaction, TransactionType, TransactionStatus, Currency
import os
from dotenv import load_dotenv
import requests


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FinanceTransactionProducer:
    def __init__(self, bootstrap_servers = os.environ['BOOTSTRAP_SERVERS'], topic = os.environ['TOPICS_NAME']):
        self.topic = topic
        self.fake = Faker()
        
        # Initialize Kafka producer
        self.producer = KafkaProducer(
            bootstrap_servers = bootstrap_servers,
            value_serializer = lambda x: json.dumps(x).encode('utf-8'),
            key_serializer = lambda x: x.encode('utf-8') if x else None
        )
        
        # Mock transaction data
        self.user_ids = [f"user_{i:06d}" for i in range(1, 10001)]  # 10k users
        self.account_ids = [f"acc_{i:08d}" for i in range(1, 50001)]  # 50k accounts
        self.merchant_ids = [f"merchant_{i:04d}" for i in range(1, 1001)]  # 1k merchants
        
        self.transaction_categories = [
            "groceries", "restaurant", "gas_station", "online_shopping", 
            "utilities", "rent", "salary", "entertainment", "healthcare",
            "education", "travel", "insurance", "investment", "loan_payment"
        ]
        
        self.locations = [
            # CNY - China
            "Beijing, China", "Shanghai, China", "Guangzhou, China", "Shenzhen, China",
            "Chengdu, China", "Hangzhou, China", "Nanjing, China", "Wuhan, China",
            "Xi'an, China", "Tianjin, China", "Chongqing, China", "Suzhou, China",
            "Qingdao, China", "Dalian, China", "Xiamen, China", "Kunming, China",
            
            # HKD - Hong Kong
            "Central, Hong Kong", "Tsim Sha Tsui, Hong Kong", "Causeway Bay, Hong Kong", "Mong Kok, Hong Kong",
            "Wan Chai, Hong Kong", "Sheung Wan, Hong Kong", "Admiralty, Hong Kong", "North Point, Hong Kong",
            "Kowloon Bay, Hong Kong", "Kwun Tong, Hong Kong", "Tsuen Wan, Hong Kong", "Sha Tin, Hong Kong",
            
            # SGD - Singapore
            "Marina Bay, Singapore", "Orchard Road, Singapore", "Raffles Place, Singapore", "Clarke Quay, Singapore",
            "Chinatown, Singapore", "Little India, Singapore", "Bugis, Singapore", "Tampines, Singapore",
            "Jurong East, Singapore", "Woodlands, Singapore", "Sengkang, Singapore", "Punggol, Singapore",
            
            # JPY - Japan
            "Tokyo, Japan", "Osaka, Japan", "Kyoto, Japan", "Yokohama, Japan",
            "Nagoya, Japan", "Sapporo, Japan", "Kobe, Japan", "Fukuoka, Japan",
            "Kawasaki, Japan", "Hiroshima, Japan", "Sendai, Japan", "Chiba, Japan",
            
            # THB - Thailand
            "Bangkok, Thailand", "Chiang Mai, Thailand", "Phuket, Thailand", "Pattaya, Thailand",
            "Krabi, Thailand", "Koh Samui, Thailand", "Hua Hin, Thailand", "Ayutthaya, Thailand",
            "Chiang Rai, Thailand", "Koh Phangan, Thailand", "Koh Tao, Thailand", "Krabi Town, Thailand",
            
            # TWD - Taiwan
            "Taipei, Taiwan", "Kaohsiung, Taiwan", "Taichung, Taiwan", "Tainan, Taiwan",
            "Hsinchu, Taiwan", "Taoyuan, Taiwan", "Keelung, Taiwan", "Chiayi, Taiwan",
            "Changhua, Taiwan", "Pingtung, Taiwan", "Yilan, Taiwan", "Hualien, Taiwan"
        ]
    
    def get_currency_rate(self, currency):
        """Fetch currency rate from API"""
        url = f"https://api.appnexus.com/currency?code={currency.value}&show_rate=true"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            rate_per_usd = data.get('response').get('currency').get('rate_per_usd')
            if rate_per_usd:
                logger.info(f"Fetched rate for {currency.value}: {rate_per_usd}")
                return rate_per_usd
            else:
                logger.warning(f"No rate found for {currency.value} in API response: {data}")
                return 0.00
        except Exception as e:
            logger.error(f"Error, cannot fetching rate for {currency.value}: {e}")
            return None

    def setting_currency_rates(self, currency):
        """Setting currency rates"""
        logger.info("Fetching currency rates from API...")
        rate = self.get_currency_rate(currency)
        logger.info(f"Set Currency rates, currency_cd: {currency.value} -> {rate}")
        return float(rate)
    
    def generate_mock_transaction(self):
        """Generate a realistic mock financial transaction"""
        
        transaction_type = random.choice(list(TransactionType))
        currency = random.choice(list(Currency))
        currency_rate = self.setting_currency_rates(currency)
        user_id = random.choice(self.user_ids)
        account_id = random.choice(self.account_ids)
        fee = 0.0
        
        # Generate amounts based on transaction type
        if transaction_type == TransactionType.TRANSFER:
            amount = random.uniform(10, 5000)
        elif transaction_type == TransactionType.DEPOSIT:
            amount = random.uniform(50, 10000)
        elif transaction_type == TransactionType.WITHDRAWAL:
            amount = random.uniform(20, 1000)
        elif transaction_type == TransactionType.PAYMENT:
            amount = random.uniform(5, 2000)
        else:
            amount = random.uniform(10, 500)

        original_amount = amount + fee
        amount = round(original_amount * currency_rate, 2)
        
        # Generate timestamp
        timestamp = datetime.now() - timedelta(
            seconds = random.randint(0, 86400 * 7) # Last 7 days
        )
        
        # Set transaction status
        status = random.choices(
            list(TransactionStatus),
            weights = [5, 90, 3, 2]  # weighting pending, completed, failed, cancelled
        )[0]
        
        # Generate description based on transaction type
        descriptions = {
            TransactionType.TRANSFER: f"Transfer to {self.fake.name()}",
            TransactionType.DEPOSIT: f"Deposit from {self.fake.company()}",
            TransactionType.WITHDRAWAL: f"ATM Withdrawal at {random.choice(self.locations)}",
            TransactionType.PAYMENT: f"Payment to {self.fake.company()}",
            TransactionType.REFUND: f"Refund from {self.fake.name()}"
        }
        
        transaction = FinancialTransaction(
            # random gen unique hash for transaction_id
            transaction_id = str(uuid.uuid4()),
            user_id = user_id,
            account_id = account_id,
            transaction_type = transaction_type,
            original_amount = original_amount,
            amount = amount,
            currency = currency,
            status = status,
            timestamp = timestamp,
            description = descriptions[transaction_type],
            recipient_account_id = random.choice(self.account_ids) if transaction_type == TransactionType.TRANSFER else None,
            recipient_user_id = random.choice(self.user_ids) if transaction_type == TransactionType.TRANSFER else None,
            fee = fee,
            currency_rate = currency_rate,
            location = random.choice(self.locations) if random.random() < 0.8 else None,
            merchant_id = random.choice(self.merchant_ids) if transaction_type == TransactionType.PAYMENT else None,
            category = random.choice(self.transaction_categories),
            reference_id = str(uuid.uuid4())[:8]
        )
        
        return transaction
    
    def produce_transactions(self, num_transactions = None, interval = None):
        """Produce mock transactions to Kafka"""
        
        logger.info(f"Starting transaction producer for topic: {self.topic}")
        
        count = 0
        try:
            while True:
                # Generate mock data and send transaction
                transaction = self.generate_mock_transaction()
                
                key = transaction.user_id
                value = transaction.to_dict()
                
                self.producer.send(
                    topic = self.topic,
                    key = key,
                    value = value
                )
                
                count += 1
                logger.info(f"Sent transaction {count}: {transaction.transaction_id} - {transaction.transaction_type.value} - ${transaction.amount} - $rate_compare_usd {transaction.currency_rate}")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logger.info("Stopping producer...")
        finally:
            # Forces Kafka brokers to write log segments from memory to disk, prevent data loss
            self.producer.flush()
            self.producer.close()
            logger.info(f"Producer stopped. Total transactions sent: {count}")

if __name__ == "__main__":    

    producer = FinanceTransactionProducer(
        bootstrap_servers = os.environ['BOOTSTRAP_SERVERS'],
        topic = os.environ['TOPICS_NAME']
    )
    
    producer.produce_transactions(num_transactions = None, interval = 2)
