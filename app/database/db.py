from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.fastapi_db
# You can define your collections here
users_collection = db.get_collection("users")


