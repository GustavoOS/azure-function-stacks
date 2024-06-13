from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("DATABASE_URL")
if url is None or url == "":
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(url)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session
session = Session()