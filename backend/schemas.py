from datetime import datetime
from pydantic import BaseModel, Field

class TransactionCreate(BaseModel):
    sender_id: str = Field(min_length=1, max_length=64)
    receiver_id: str = Field(min_length=1, max_length=64)
    amount: float = Field(gt=0, le=100000000)
    timestamp: datetime | None = None

