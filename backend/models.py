from datetime import datetime, timezone
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

def utcnow(): return datetime.now(timezone.utc)

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    risk_score: Mapped[float] = mapped_column(Float, default=0)
    is_potential_mule: Mapped[int] = mapped_column(Integer, default=0)

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    sender_id: Mapped[str] = mapped_column(ForeignKey("accounts.id"), index=True)
    receiver_id: Mapped[str] = mapped_column(ForeignKey("accounts.id"), index=True)
    amount: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, index=True)
    status: Mapped[str] = mapped_column(String, default="completed")
    fraud_probability: Mapped[float] = mapped_column(Float, default=0)
    risk_score: Mapped[float] = mapped_column(Float, default=0)
    classification: Mapped[str] = mapped_column(String, default="Legitimate Transaction")
    detection_reason: Mapped[str] = mapped_column(Text, default="No elevated risk indicators")

class FraudAlert(Base):
    __tablename__ = "fraud_alerts"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    transaction_id: Mapped[str] = mapped_column(ForeignKey("transactions.id"), index=True)
    account_id: Mapped[str] = mapped_column(String, index=True)
    amount: Mapped[float] = mapped_column(Float)
    fraud_probability: Mapped[float] = mapped_column(Float)
    risk_level: Mapped[str] = mapped_column(String)
    detection_reason: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

class ModelLog(Base):
    __tablename__ = "model_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    transaction_id: Mapped[str] = mapped_column(String, index=True)
    fraud_probability: Mapped[float] = mapped_column(Float)
    classification: Mapped[str] = mapped_column(String)
    model_version: Mapped[str] = mapped_column(String, default="synthetic-rf-v1")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
