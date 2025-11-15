# database.py
import datetime
from pymongo import MongoClient
import config

# Connect to MongoDB
client = MongoClient(config.MONGO_URI)
db = client['donation_bot_db']
# We use two collections: one for raw logs, one for aggregated user stats
donations_collection = db['donations_log']
users_collection = db['users']

def record_donation(user_id: int, first_name: str, username: str, amount: int, tier: str):
    """Logs a new donation and updates the user's total donations."""
    
    # 1. Log the individual donation event
    donations_collection.insert_one({
        "user_id": user_id,
        "amount": amount,
        "tier": tier,
        "timestamp": datetime.datetime.utcnow()
    })

    # 2. Update the user's aggregated stats
    # Using $inc to add to existing total, and $set to update other info
    # upsert=True creates the document if it doesn't exist
    users_collection.update_one(
        {"user_id": user_id},
        {
            "$inc": {"total_donated": amount},
            "$set": {
                "first_name": first_name,
                "username": username,
                "last_tier_donated": tier,
                "last_donated_timestamp": datetime.datetime.utcnow()
            }
        },
        upsert=True
    )

def get_user_stats(user_id: int):
    """Retrieves donation statistics for a single user."""
    return users_collection.find_one({"user_id": user_id})

def get_leaderboard(limit: int = 10):
    """Retrieves the top N donators from the database."""
    # Find users, sort by total_donated in descending order, and limit the result
    return list(
        users_collection.find().sort("total_donated", -1).limit(limit)
    )
