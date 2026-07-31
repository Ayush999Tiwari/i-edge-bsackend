from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    services_access = Column(
        JSONB, 
        default=lambda: ["egg_counting", "surveillance"]
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())