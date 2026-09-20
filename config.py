# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import os

def must_get(name):
    value = os.getenv(name)
    if not value:
        raise Exception(f"{name} is not set in environment variables")
    return value

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

API_ID = int(must_get("API_ID"))
API_HASH = must_get("API_HASH")
BOT_TOKEN = must_get("BOT_TOKEN")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

MONGO_URI = must_get("MONGO_URI")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

BOT_USERNAME = must_get("BOT_USERNAME")

CHANNEL_ID = int(must_get("CHANNEL_ID"))

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

OWNER_ID = int(must_get("OWNER_ID"))

LOG_CHANNEL = int(must_get("LOG_CHANNEL"))

PORT = int(os.getenv("PORT", "10000"))

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

FORCE_SUB_IMAGE = os.getenv(
    "FORCE_SUB_IMAGE",
    "https://graph.org/file/14c3a336058422b14549d-85d887f6fd8a9cead5.jpg"
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

CHECKING_IMAGE = os.getenv(
    "CHECKING_IMAGE",
    "https://graph.org/file/c658f88f509dd0c786ac5-44bdf2692f1ca00b29.jpg"
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

ADMINLIST_IMAGE = os.getenv(
    "ADMINLIST_IMAGE",
    "https://graph.org/file/51f7bf1769486242f1180-03990f535eec7e1aba.jpg"
)

# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #

INDEX_IMAGE = os.getenv(
    "INDEX_IMAGE",
    "https://graph.org/file/d8a01f513fb925e5a0743-17d6591665bbca7517.jpg"
)

# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #
