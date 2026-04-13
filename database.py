from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.filebot

files = db.files
users = db.users

# FILES
async def save_file(file_id, file_unique_id, file_type, caption):
    await files.update_one(
        {"file_unique_id": file_unique_id},
        {"$set": {
            "file_id": file_id,
            "file_unique_id": file_unique_id,
            "file_type": file_type,
            "caption": caption
        }},
        upsert=True
    )
    
async def get_file(file_unique_id):
    return await files.find_one({"file_unique_id": file_unique_id})

# USERS
async def add_user(user_id):
    await users.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def get_all_users():
    return users.find()

async def total_users():
    return await users.count_documents({})
