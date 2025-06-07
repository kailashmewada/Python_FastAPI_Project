from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv(override=True)

MONGO_URI= os.getenv("MONGO_URI", "mongodb://localhost:27017/fastapi_db")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "fastapi_db")
DATABASE_NAME= os.getenv("DATABASE_NAME", "fastapi_db")    
SECRET_KEY= os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM= os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))