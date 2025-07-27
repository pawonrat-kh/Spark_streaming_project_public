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
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            transaction_id=data["transaction_id"],
            user_id=data["user_id"],
            account_id=data["account_id"],
            transaction_type=TransactionType(data["transaction_type"]),
            original_amount=data["original_amount"],
            amount=data["amount"],
            currency=Currency(data["currency"]),
            status=TransactionStatus(data["status"]),
            timestamp=datetime.fromisoformat(data["timestamp"]),
            description=data["description"],
            recipient_account_id=data.get("recipient_account_id"),
            recipient_user_id=data.get("recipient_user_id"),
            fee=data.get("fee"),
            currency_rate=data.get("currency_rate"),
            location=data.get("location"),
            merchant_id=data.get("merchant_id"),
            category=data.get("category"),
            reference_id=data.get("reference_id")
        )
