from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
from datetime import datetime

client = AsyncIOMotorClient(MONGO_URI)
db = client.filebot

files = db.files
users = db.users
admins = db["admins"]

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
    if not user_id:
        return

    await users.update_one(
        {"user_id": int(user_id)},
        {"$setOnInsert": {"user_id": int(user_id)}},
        upsert=True
    )

async def get_all_users():
    users_list = []
    async for user in users.find():
        users_list.append(user["user_id"])
    return users_list
    

async def total_users():
    return await users.count_documents({})

# ADMIN SYSTEM

async def add_admin_db(user_id, name, username):

    user_id = int(user_id)

    await admins.update_one(
        {"user_id": user_id},
        {"$set": {
            "user_id": user_id,
            "name": name,
            "username": username,
            "joined_date": datetime.now().strftime("%d-%m-%Y %H:%M")
        }},
        upsert=True
    )

async def get_all_admins():
    admins_list = []
    async for admin in admins.find():
        admins_list.append(admin)
    return admins_list

async def remove_admin_db(user_id):
    await admins.delete_one({"user_id": int(user_id)})

async def is_admin(user_id):
    user_id = int(user_id)

    data = await admins.find_one({"user_id": user_id})

    return bool(data)
