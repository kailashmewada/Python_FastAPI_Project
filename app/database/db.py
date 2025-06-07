from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.fastapi_db
# You can define your collections here
users_collection = db.get_collection("users")


