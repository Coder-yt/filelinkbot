
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import *
from pyrogram.types import InputMediaPhoto
from pyrogram.enums import ParseMode, ChatMemberStatus
from pyrogram.errors import FloodWait, UserNotParticipant

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import shutil 
from pymongo import DESCENDING
from deep_translator import GoogleTranslator

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import os
import sys
import platform
import random
import psutil

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import time
import gc
import asyncio 
import speedtest
import logging
import pytz
import syncedlyrics

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

LYRICS_CACHE = {}
MAX_CHARS = 3500
TIMEZONE = "Asia/Kolkata"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def split_lyrics(text, size=MAX_CHARS):
    pages = []
    while len(text) > size:
        cut = text.rfind("\n", 0, size)
        if cut == -1:
            cut = size
        pages.append(text[:cut])
        text = text[cut:].strip()
    if text:
        pages.append(text)
    return pages

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def get_lyrics(song_name):
    """
    Fetch lyrics in the original language.
    """
    try:
        lyrics = syncedlyrics.search(song_name)

        if not lyrics:
            return None

        # Remove timestamps if present
        clean = []
        for line in lyrics.splitlines():
            if "] " in line:
                line = line.split("] ", 1)[1]
            clean.append(line)

        return "\n".join(clean).strip()

    except Exception:
        return None

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #