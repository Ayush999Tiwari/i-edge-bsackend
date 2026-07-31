from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# convert postgres:// -> postgresql+asyncpg:// if needed
DATABASE_URL = DATABASE_URL.replace(
    "postgresql://",
    "postgresql+asyncpg://",
    1
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)

Base = declarative_base()