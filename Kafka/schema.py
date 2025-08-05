from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from enum import Enum
import json

class TransactionType(Enum):
    TRANSFER = "transfer"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    PAYMENT = "payment"
    REFUND = "refund"

class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class Currency(Enum):
    CNY = "CNY"
    HKD = "HKD"
    SGD = "SGD"
    JPY = "JPY"
    THB = "THB"
    TWD = "TWD"

@dataclass
class FinancialTransaction:
    transaction_id: str
    user_id: str
    account_id: str
    transaction_type: TransactionType
    original_amount: float
    amount: float
    currency: Currency
    status: TransactionStatus
    timestamp: datetime
    description: str
    recipient_account_id: Optional[str] = None
    recipient_user_id: Optional[str] = None
    fee: float = 0.0
    currency_rate: float = 0.0
    location: Optional[str] = None
    merchant_id: Optional[str] = None
    category: Optional[str] = None
    reference_id: Optional[str] = None
    
    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "account_id": self.account_id,
            "transaction_type": self.transaction_type.value,
            "original_amount": self.original_amount,
            "amount": self.amount,
            "currency": self.currency.value,
            "status": self.status.value,
            "timestamp": self.timestamp.isoformat(),
            "description": self.description,
            "recipient_account_id": self.recipient_account_id,
            "recipient_user_id": self.recipient_user_id,
            "fee": self.fee,
            "currency_rate": self.currency_rate,
            "location": self.location,
            "merchant_id": self.merchant_id,
            "category": self.category,
            "reference_id": self.reference_id
        }
