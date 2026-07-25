
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

logging.basicConfig(level=logging.INFO)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

IMAGES = [
    "AgACAgUAAxkBAAIHiWpiB1zFmP1eQSpb5TUztD0UKoDdAAI7GWsblIMIV43SgSB8TbQyAAgBAAMCAAN3AAceBA",
    "AgACAgUAAxkBAAIHi2piCw1SzmzOMAWDjV-yvd73IOQ0AAKDE2sblIMQV-Hxw982KnNVAAgBAAMCAAN5AAceBA",
    "AgACAgUAAxkBAAIHjWpiCxpIuLdo7rDcJN9ESUQsAAGM5QACPRJrG5NGsVYJAoYha3x6rgAIAQADAgADeQAHHgQ",
    "AgACAgUAAxkBAAIHj2piCyPqgt7BK5fXiyeZNVYmbT3AAAK1FGsb0zHAVs3uxQOJqpNyAAgBAAMCAAN5AAceBA"
]

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from database import (
    save_file,
    get_file,
    increase_single_links,
    increase_batch_links,
    get_link_stats,
    increase_download,
    add_user,
    get_all_users,
    total_users,
    total_files, 
    total_admins,
    add_admin_db,
    remove_admin_db,
    is_admin,
    get_all_admins,
    add_force_sub,
    remove_force_sub,
    get_force_subs,
    files,
    users,
    verify_db,
    save_verify,
    get_verify,
    delete_verify,
    ban_user,
    unban_user,
    is_banned,
    get_file_by_unique_id,
    today_files,
    week_files,
    add_database,
    get_all_databases,
    get_active_database as get_saved_active_database,
    set_active_database
)

from multidb import (
    load_database,
    total_databases,
    remove_database as remove_loaded_db,
    has_database,
    database_list,
    get_active_database,
    switch_database,
    database_status,
    get_active_database
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from keep_alive import keep_alive

START_TIME = time.time()
BOT_VERSION = "v3.0"
CACHE = {}
MAINTENANCE = False

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def format_size(size):
    power = 1024
    units = ["B", "KB", "MB", "GB", "TB"]

    n = 0
    while size > power and n < len(units) - 1:
        size /= power
        n += 1

    return f"{size:.2f} {units[n]}"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

app = Client(
    "filelinkbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
) 

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def send_log(text):
    try:
        await app.send_message(
            LOG_CHANNEL,
            text,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(e)
        
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import base64
import re

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

BATCH_USERS = {}
INDEX_CACHE = {}

# ------------------------- #
# INDEX SYSTEM
# ------------------------- #

LETTERS = [
    "A","B","C","D","E","F","G",
    "H","I","J","K","L","M","N",
    "O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"
]

# ================= GET MESSAGE ID =================

async def get_message_id(client, link):

    try:
        link = link.strip()

        if "/c/" in link:

            parts = link.split("/")

            chat_id = int("-100" + parts[-2])
            msg_id = int(parts[-1])

            return chat_id, msg_id

        match = re.search(r"t\.me/([^/]+)/(\d+)", link)

        if match:

            username = match.group(1)
            msg_id = int(match.group(2))

            chat = await client.get_chat(username)

            return chat.id, msg_id

        return None, None

    except:
        return None, None


# ================= BATCH COMMAND =================

@app.on_message(filters.command("batch") & filters.private)
async def batch_command(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "**🚫 You are banned from using this bot.**"
        )

    user_id = message.from_user.id

    if user_id != OWNER_ID and not await is_admin(user_id):

        return await message.reply_text(
            "**ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!**."
        )

    BATCH_USERS[user_id] = {
        "step": "first"
    }

    await message.reply_text(
        "🔗 Gɪᴠᴇ Mᴇ Bᴀᴛᴄʜ Fɪʀsᴛ Mᴇssᴀɢᴇ 𝗟𝗶𝗻𝗸 ғʀᴏᴍ ʏᴏᴜʀ 𝗗𝗕 ᴄʜᴀɴɴᴇʟ"
    )


# ================= HANDLE BATCH =================

@app.on_message(
    filters.private &
    filters.text &
    ~filters.command([
        "start",
        "batch",
        "stats",
        "broadcast",
        "addadmin",
        "removeadmin",
        "adminlist",
        "addfsub",
        "removefsub",
        "fsublist",
        "index",
        "ban",
        "unban",
        "banlist",
        "alive",
        "id",
        "system", 
        "restart",
        "disclaimer",
        "speedtest",
        "adddb",
        "removedb",
        "dblist",
        "dbstatus",
        "lyrics",
        "translate"
    ])
)
async def handle_batch(client, message):

    user_id = message.from_user.id

    if user_id not in BATCH_USERS:
        return

    data = BATCH_USERS[user_id]

    # FIRST LINK
    if data["step"] == "first":

        chat_id, first_msg_id = await get_message_id(
            client,
            message.text
        )

        if not first_msg_id:

            return await message.reply_text(
                "‼️ Iɴᴠᴀʟɪᴅ Fɪʀsᴛ Lɪɴᴋ"
            )

        data["chat_id"] = chat_id
        data["first_msg_id"] = first_msg_id
        data["step"] = "last"

        return await message.reply_text(
            "🔗 Gɪᴠᴇ Mᴇ Bᴀᴛᴄʜ Lᴀsᴛ Mᴇssᴀɢᴇ 𝗟𝗶𝗻𝗸 ғʀᴏᴍ ʏᴏᴜʀ 𝗗𝗕 ᴄʜᴀɴɴᴇʟ"
        )

    # LAST LINK
    elif data["step"] == "last":

        chat_id, last_msg_id = await get_message_id(
            client,
            message.text
        )

        if not last_msg_id:

            return await message.reply_text(
                "‼️ Iɴᴠᴀʟɪᴅ Lᴀsᴛ Lɪɴᴋ"
            )

        first_msg_id = data["first_msg_id"]

        if last_msg_id < first_msg_id:

            return await message.reply_text(
                "‼️ Lᴀsᴛ ᴍᴇssᴀɢᴇ ᴍᴜsᴛ ʙᴇ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ ғɪʀsᴛ ᴍᴇssᴀɢᴇ"
            )

        batch_data = (
            f"batch:{data['chat_id']}:{first_msg_id}:{last_msg_id}"
        )

        encoded = base64.urlsafe_b64encode(
            batch_data.encode("utf-8")
        ).decode("utf-8")

        bot_username = (await client.get_me()).username

        link = f"https://t.me/{bot_username}?start={encoded}"

        await increase_batch_links()

        await message.reply_text(
            f"✅ ʙᴀᴛᴄʜ ʟɪɴᴋs ɢᴇɴᴇʀᴀᴛᴇᴅ\n\n{link}"
        )

        del BATCH_USERS[user_id]

# ------------------------- #
# FORCE SUBSCRIBE CHECK
# ------------------------- #

async def check_force_sub(client, user_id):

    channels = await get_force_subs()

    if not channels:
        return True, None

    buttons = []

    for channel in channels:

        try:
            chat = await client.get_chat(channel)
        except Exception:
            # Invalid/deleted channel in DB
            try:
                await remove_force_sub(channel)
            except:
                pass
            continue

        try:
            member = await client.get_chat_member(chat.id, user_id)

            if member.status in (
                ChatMemberStatus.LEFT,
                ChatMemberStatus.BANNED
            ):
                raise UserNotParticipant

        except UserNotParticipant:

            if chat.username:
                link = f"https://t.me/{chat.username}"
            else:
                try:
                    invite = await client.create_chat_invite_link(
                        chat.id,
                        member_limit=1
                    )
                    link = invite.invite_link
                except:
                    continue

            buttons.append([
                InlineKeyboardButton(
                    chat.title,
                    url=link
                )
            ])

        except Exception:
            continue

    if buttons:
        buttons.append([
            InlineKeyboardButton(
                "• ᴛʀʏ ᴀɢᴀɪɴ •",
                callback_data="checksub"
            )
        ])

        return False, InlineKeyboardMarkup(buttons)

    return True, None
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.photo & filters.private & filters.user(OWNER_ID))
async def get_photo_id(client, message):
    await message.reply_text(
        f"<b>Photo or Image or Pic File ID:</b>\n\n<code>{message.photo.file_id}</code>"
    )

# START + LINK HANDLER
@app.on_message(filters.command("start"))
async def start(client, message: Message):

    user_id = message.from_user.id

    if await is_banned(user_id):
        return await message.reply_text(
            "🚫 **You are banned from using this bot.**\n\n"
            "**If you believe this is a mistake, contact the "
            "[Owner](https://t.me/Mr_Mohammed_29).**",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )

    await add_user(user_id)

    # Save parameter before Force Subscribe check
    if len(message.command) > 1:
        param = message.command[1]
        await save_verify(user_id, param)

    user = message.from_user

    await send_log(
        f"**ɴᴇᴡ ᴜsᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ**\n\n"
        f"👤 **{user.first_name}**\n"
        f"🆔 **`{user.id}`**\n"
        f"📛 **@{user.username if user.username else 'None'}**"
    )

    # ------------------------- #
    # FORCE SUBSCRIBE CHECK
    # ------------------------- #

    ok, keyboard = await check_force_sub(
        client,
        user_id
    )

    if not ok:
        return await message.reply_photo(
            photo=FORCE_SUB_IMAGE,
            caption=(
                "**›› ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ...**\n\n"
                "• ᴘʀᴇss **ᴛʀʏ ᴀɢᴀɪɴ**."
            ),
            reply_markup=keyboard,
            parse_mode=ParseMode.MARKDOWN
        )

    # START ANIMATION
    m = await message.reply_text("ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻. . .")
    await asyncio.sleep(0.5)
    await m.edit_text("🔥")
    await asyncio.sleep(0.5)
    await m.edit_text("⚡")
    await asyncio.sleep(0.5)
    await m.edit_text("sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...")
    await asyncio.sleep(0.5)
    await m.delete()

    if len(message.command) > 1:
        param = message.command[1]

        # ================= BATCH LINK =================

        try:

            decoded = base64.urlsafe_b64decode(
                param + "=" * (-len(param) % 4)
            ).decode("utf-8", errors="ignore")

            if decoded.startswith("batch:"):

                _, chat_id, first_id, last_id = decoded.split(":")

                chat_id = int(chat_id)
                first_id = int(first_id)
                last_id = int(last_id)

                sent_messages = []

                wait = await message.reply_text("⏳ sᴇɴᴅɪɴɢ ғɪʟᴇs...")

                for msg_id in range(first_id, last_id + 1):

                    try:
                        msg = await client.get_messages(chat_id, msg_id)

                        if not msg:
                            continue

                        original_caption = msg.caption if msg.caption else ""

                        caption = (
                            f"**{original_caption}**\n\n"
                            f"**›› ʙʏ : [ᴀᴇʀᴏ ᴜɴɪᴛʏ](https://t.me/Aero_Unity)**"
                        )

                        buttons = InlineKeyboardMarkup(
                            [[InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity")]]
                        )

                        if msg.video:
                            sent = await message.reply_video(
                                video=msg.video.file_id,
                                caption=caption,
                                reply_markup=buttons,
                                supports_streaming=True,
                                parse_mode=ParseMode.MARKDOWN
                            )

                        elif msg.audio:
                            sent = await message.reply_audio(
                                audio=msg.audio.file_id,
                                caption=caption,
                                reply_markup=buttons,
                                parse_mode=ParseMode.MARKDOWN
                            )

                        elif msg.document:
                            sent = await message.reply_document(
                                document=msg.document.file_id,
                                caption=caption,
                                reply_markup=buttons,
                                parse_mode=ParseMode.MARKDOWN
                            ) 

                        elif msg.sticker:
                            sent = await message.reply_sticker(sticker=msg.sticker.file_id)

                        elif msg.animation:
                           sent = await message.reply_animation(
                               animation=msg.animation.file_id,
                               caption=caption,
                               reply_markup=buttons,
                               parse_mode=ParseMode.MARKDOWN
                           )
                        else:
                            continue

                        sent_messages.append(sent)

                        try:
                            unique_id = None

                            if msg.video:
                                unique_id = msg.video.file_unique_id
                            elif msg.document:
                                unique_id = msg.document.file_unique_id
                            elif msg.audio:
                                unique_id = msg.audio.file_unique_id
                            elif msg.animation:
                                unique_id = msg.animation.file_unique_id

                            if unique_id:
                                await increase_download(unique_id)

                        except Exception:
                           pass

                        await asyncio.sleep(0.3)

                    except Exception as e:
                        print(e)

                await wait.delete()

                await send_log(
                    f"📦 **Bᴀᴛᴄʜ Aᴄᴄᴇss**\n\n"
                    f"👤 {message.from_user.mention}\n"
                    f"🆔 `{message.from_user.id}`\n"
                    f"Messages: {first_id} - {last_id}"
                )

                warn = await message.reply_text(
                    " **⏳ Dᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs...**\n\n"
                    " **›› Yᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ 𝟻 ᴍɪɴᴜᴛᴇs.**\n"
                    " **›› Sᴏ ᴘʟᴇᴀsᴇ sᴀᴠᴇ ᴛʜᴇᴍ.**",
                    parse_mode=ParseMode.MARKDOWN
                )

                await asyncio.sleep(300)

                for x in sent_messages:
                    try:
                        await x.delete()
                    except:
                        pass

                try:
                    await warn.delete()
                except:
                    pass
 
                return

        except Exception as e:
            return

        file_unique_id = message.command[1]
        data = await get_file(file_unique_id)

        if not data:
            return await message.reply_text("🔎 Fɪʟᴇ Is Nᴏᴛ Fᴏᴜɴᴅ, Cᴏɴᴛᴀᴄᴛ Tᴏ Oᴡɴᴇʀ.")

        original_caption = data.get("caption", "")
        caption = (
    f"**{original_caption}**\n\n"
    f"**›› ʙʏ :[ᴀᴇʀᴏ ᴜɴɪᴛʏ](https://t.me/Aero_Unity)**"
)

        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity")]]
        )

        if data.get("file_type") == "video":
            sent = await message.reply_video(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                thumb=data.get("thumb") if data.get("thumb") else None,
                supports_streaming=True,
                parse_mode=ParseMode.MARKDOWN
        ) 

        elif data.get("file_type") == "audio":
            sent = await message.reply_audio(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                parse_mode=ParseMode.MARKDOWN
        )

        elif data.get("file_type") == "document":
            sent = await message.reply_document(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                parse_mode=ParseMode.MARKDOWN
        )

        elif data.get("file_type") == "sticker":
            sent = await message.reply_sticker(
                data["file_id"]
        )

        elif data.get("file_type") == "animation":  # GIF
            sent = await message.reply_animation(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                parse_mode=ParseMode.MARKDOWN
        )

        else:
            return await message.reply_text("‼️ Unsupported format")

        await increase_download(file_unique_id)

        await delete_verify(user_id)

        await send_log(
            f"📥 **Fɪʟᴇ Aᴄᴄᴇssᴇᴅ**\n\n"
            f"👤 {message.from_user.mention}\n"
            f"🆔 `{message.from_user.id}`\n"
            f"📂 {data.get('caption','No Caption')}"
        )

        warn = await message.reply_text(
    " **⏳ Dᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs...**\n\n"
    " **›› Yᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ 𝟻 ᴍɪɴᴜᴛᴇs.**\n"
    " **›› Sᴏ ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜᴇᴍ ᴛᴏ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs.**\n\n"
    " ›› 𝗡𝗼𝘁𝗲: ᴜsᴇ **𝗩𝗟𝗖 𝗣𝗹𝗮𝘆𝗲𝗿** ᴏʀ **𝗠𝗫 𝗣𝗹𝗮𝘆𝗲𝗿** ғᴏʀ ʙᴇsᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ.",
    parse_mode=ParseMode.MARKDOWN
        )

        # AFTER FILE ANIMATION
        m2 = await message.reply_text("ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻. . .")
        await asyncio.sleep(0.4)
        await m2.edit_text("sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...")
        await asyncio.sleep(0.5)
        await m2.delete()

        await asyncio.sleep(300)

        try:
            await sent.delete()
        except:
            pass

        try:
            await warn.delete()
        except:
            pass

        return

    # START MESSAGE WITH BUTTONS
    photo = random.choice(IMAGES)

    await message.reply_photo(
        photo=photo,
        caption=(
            "𝗛𝗲𝗹𝗹𝗼 ♡,\n\n"
            "›› 𝗜 𝗰𝗮𝗻 𝘀𝘁𝗼𝗿𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝗦𝗽𝗲𝗰𝗶𝗳𝗶𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝗼𝘁𝗵𝗲𝗿 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗮𝗰𝗰𝘀𝘀 𝗶𝘁 𝗳𝗿𝗼𝗺 𝘀𝗽𝗲𝗰𝗶𝗮𝗹 𝗹𝗶𝗻𝗸."
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity"),
                    InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="about")
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/Mr_Mohammed_29")
                ]
            ]
        ),
        parse_mode=ParseMode.MARKDOWN
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ONLY OWNER + ADMIN CAN UPLOAD 
@app.on_message(
    (filters.document | filters.video | filters.audio | filters.sticker | filters.animation) &
    filters.private
)
async def save_media(client, message: Message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"
        )

    # Allow only owner + admin
    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text(" ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃..")

    original_caption = message.caption if message.caption else ""

    # Detect file type
    if message.video:
        file = message.video
        file_type = "video"
        thumb = None
        if hasattr(file, "thumbs") and file.thumbs:
            thumb = file.thumbs[-1].file_id

    elif message.audio:
        file = message.audio
        file_type = "audio"
        thumb = None

    elif message.document:
        file = message.document
        file_type = "document"
        thumb = None

    elif message.sticker:
        file = message.sticker
        file_type = "sticker"
        thumb = None

    elif message.animation:  # GIF
        file = message.animation
        file_type = "animation"
        thumb = None

    else:
        return await message.reply_text("‼️ Uɴsᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛ")

    file_id = file.file_id
    file_unique_id = file.file_unique_id

    await save_file(
        file_id=file_id,
        file_unique_id=file_unique_id,
        file_type=file_type,
        caption=original_caption,
        thumb=thumb,
        file_name=getattr(file, "file_name", ""),
        file_size=getattr(file, "file_size", 0),
        uploader_id=message.from_user.id
    )

    await send_log(
        f"📤 **Nᴇᴡ Fɪʟᴇ Uᴘʟᴏᴀᴅᴇᴅ**\n\n"
        f"👤 {message.from_user.mention}\n"
        f"🆔 `{message.from_user.id}`\n"
        f"📁 {getattr(file, 'file_name', file_type)}"
    )

    await increase_single_links()

    link = f"https://t.me/{BOT_USERNAME}?start={file_unique_id}"
    
    await message.reply_text(f"🔗 𝗛𝗲𝗿𝗲 𝗜𝘀 𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸:\n{link}")
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# STATS
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(client, message: Message):

    msg = await message.reply_text(
        "<b>Extracting Bot Statistics...</b>",
        parse_mode=ParseMode.HTML
    )

    start = time.time()

    total = await total_users()
    total_files_count = await total_files()
    single_links, batch_links = await get_link_stats()

    uptime_seconds = int(time.time() - START_TIME)
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    ping = round((time.time() - start) * 1000, 3)

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    def progress(percent):
        filled = int(percent // 10)
        return "■" * filled + "▤" + "□" * (9 - filled)

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ", callback_data="refresh_stats")]
        ]
    )

    await msg.edit_text(
        f"""⌬ <b>𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗜𝗦𝗧𝗜𝗖𝗦 :</b>

┎ <b>Bᴏᴛ Uᴘᴛɪᴍᴇ :</b> {hours}h {minutes}m {seconds}s
┃ <b>Cᴜʀʀᴇɴᴛ Pɪɴɢ :</b> {ping} ms
┖ <b>Tᴏᴛᴀʟ Uꜱᴇʀꜱ :</b> {total}

┎ <b>RAM ( MEMORY ) :</b>
┖ [{progress(ram.percent)}] {ram.percent}%

┎ <b>CPU ( USAGE ) :</b>
┖ [{progress(cpu)}] {cpu}%

┎ <b>DISK :</b>
┃ [{progress(disk.percent)}] {disk.percent}%
┃ <b>Usᴇᴅ :</b> {disk.used / (1024**3):.2f} GB
┃ <b>Fʀᴇᴇ :</b> {disk.free / (1024**3):.2f} GB
┖ <b>Tᴏᴛᴀʟ :</b> {disk.total / (1024**3):.2f} GB

┎ <b>Fɪʟᴇ Sᴛᴏʀᴇ :</b>
┃ <b>Tᴏᴛᴀʟ Fɪʟᴇs :</b> {total_files_count}
┃ <b>Sɪɴɢʟᴇ Lɪɴᴋs :</b> {single_links}
┖ <b>Bᴀᴛᴄʜ Lɪɴᴋs :</b> {batch_links}
""",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# BROADCAST
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message: Message):

    if not message.reply_to_message:
        return await message.reply_text("Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ..")

    msg = message.reply_to_message

    users = await get_all_users()

    sent = 0
    failed = 0

    status = await message.reply_text("⏳️ 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱.....")  

    for user_id in users:
        try:
            await msg.copy(chat_id=int(user_id))
            sent += 1
            await asyncio.sleep(0.05)

        except FloodWait as e:
            await asyncio.sleep(e.value)

        except Exception as e:
            failed += 1
            print(f"Failed: {user_id} | {e}")

    await status.edit_text(
        f"⏳️ 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗖𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱\n\n"
        f"◇ Sᴜᴄᴄᴇssғᴜʟ: {sent}\n"
        f"◇ Uɴsᴜᴄᴄᴇssғᴜʟ: {failed}"
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
    
@app.on_message(
    filters.private &
    ~filters.service &
    ~filters.command([
        "start",
        "batch",
        "stats",
        "broadcast",
        "addadmin",
        "removeadmin",
        "adminlist",
        "addfsub",
        "removefsub",
        "fsublist",
        "index",
        "ban",
        "unban",
        "banlist",
        "alive",
        "id",
        "system",
        "restart",
        "disclaimer",
        "speedtest",
        "adddb",
        "removedb",
        "dblist",
        "dbstatus",
        "lyrics",
        "translate"
        
    ])
)
async def auto_add_user(client, message):

    if message.from_user and await is_banned(message.from_user.id):
        return
        
    if message.from_user:
        await add_user(message.from_user.id)
        
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ADD ADMIN 
@app.on_message(filters.command("addadmin") & filters.private)
async def add_admin(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text("ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!..")

    if len(message.command) < 2:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ /addadmin user_id")

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("‼️ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ ɪᴅ")

    user = await client.get_users(user_id)

    name = user.first_name
    username = user.username if user.username else "None"

    await add_admin_db(user_id, name, username)

    await message.reply_text(f"✅️ ᴀᴅᴍɪɴ ɪs ᴀᴅᴅᴇᴅ : {user_id}")

    # Send message to that user
    try:
        await client.send_message(
            chat_id=user_id,
            text="🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴘʀᴏᴍᴏᴛᴇᴅ ᴛᴏ 𝗔𝗗𝗠𝗜𝗡\n\nYᴏᴜ ᴄᴀɴ ɴᴏᴡ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ʟɪɴᴋs."
        )
    except Exception as e:
        print(f"Fᴀɪʟᴇᴅ Tᴏ Nᴏᴛɪғʏ Aᴅᴍɪɴ : {e}")
        
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# REMOVE ADMIN 
@app.on_message(filters.command("removeadmin") & filters.private)
async def remove_admin(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text("ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!.")

    if len(message.command) < 2:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ /removeadmin user_id")

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("‼️ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ ɪᴅ")

    await remove_admin_db(user_id)

    await message.reply_text(f"✅️ ᴀᴅᴍɪɴ ɪs ʀᴇᴍᴏᴠᴇᴅ : {user_id}")
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

#ADMIN LIST
@app.on_message(filters.command("adminlist") & filters.private)
async def admin_list(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "**ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!..**"
        )

    admins = await get_all_admins()

    if not admins:
        return await message.reply_text(
            "‼️ Nᴏ Aᴅᴍɪɴs Fᴏᴜɴᴅ Iɴ Lɪsᴛ"
        )

    text = "👑 Aᴅᴍɪɴ Lɪsᴛ\n\n"

    for i, admin in enumerate(admins, start=1):

        name = admin.get("name", "Unknown")
        username = admin.get("username", "None")
        user_id = admin.get("user_id")

        text += (
            f"{i}. 𝗡𝗮𝗺𝗲: {name}\n"
            f"  𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: @{username if username != 'None' else 'no_username'}\n"
            f"  𝗜𝗗: {user_id}\n\n"
        )

    await message.reply_photo(
        photo=ADMINLIST_IMAGE,
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
    
@app.on_message(filters.command("index") & filters.private)
async def index_command(client, message):

    if not (
        message.from_user.id == OWNER_ID
        or await is_admin(message.from_user.id)
    ):
        return await message.reply_text(
            "**ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!**"
        )

    rows = []

    for i in range(0, 26, 4):
        row = []

        for letter in LETTERS[i:i+4]:
            row.append(
                InlineKeyboardButton(
                    letter,
                    callback_data=f"index_{letter}"
                )
            )

        rows.append(row)

    rows.append(
        [
            InlineKeyboardButton(
                "• ᴄʟᴏsᴇ •",
                callback_data="close"
            )
        ]
    )

    await message.reply_photo(
        photo=INDEX_IMAGE,
        caption=(
            " **Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Iɴᴅᴇx**\n\n"
            "**Sᴇʟᴇᴄᴛ ᴀ ʟᴇᴛᴛᴇʀ ᴛᴏ ᴠɪᴇᴡ ᴄʜᴀɴɴᴇʟs.**"
        ),
        reply_markup=InlineKeyboardMarkup(rows)
    )

# ------------------------- #
# INDEX LETTER CALLBACK
# ------------------------- #

@app.on_callback_query(filters.regex(r"^index_([A-Z])$"))
async def index_letter_callback(client, query):

    letter = query.data.split("_")[1]

    channels = await get_force_subs()

    text = f"**ᴄʜᴀɴɴᴇʟs sᴛᴀʀᴛɪɴɢ ᴡɪᴛʜ {letter}**\n\n"

    found = False

    for i, ch in enumerate(channels, start=1):

        try:
            chat = await client.get_chat(ch)

            if not chat.title.upper().startswith(letter):
                continue

            found = True

            if chat.username:
                text += (
                    f"**{i}.** @{chat.username}\n"
                    f"**ID:** `{chat.id}`\n\n"
                )
            else:
                text += (
                    f"**{i}.** {chat.title}\n"
                    f"**ID:** `{chat.id}`\n\n"
                )

        except:
            continue

    if not found:
        text += "**Nᴏ ᴄʜᴀɴɴᴇʟs ғᴏᴜɴᴅ ᴏʀ ᴀᴅᴅᴇᴅ**"

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "• ʙᴀᴄᴋ •",
                    callback_data="index_back"
                ),
                InlineKeyboardButton(
                    "• ᴄʟᴏsᴇ •",
                    callback_data="close"
                )
            ]
        ]
    )

    await query.message.edit_caption(
        caption=text,
        reply_markup=keyboard
    )
    
# ------------------------- #
# FORCE SUBSCRIBE COMMANDS
# ------------------------- #

@app.on_message(filters.command("ban") & filters.private)
async def ban(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/ban user_id"
        )

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("Invalid User ID")

    await ban_user(user_id)

    await message.reply_text(
        f"✅ User `{user_id}` has been banned."
    )

    try:
        await client.send_message(
            user_id,
            "**🚫 You have been banned from using this bot.**"
        )
    except:
        pass

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("unban") & filters.private)
async def unban(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/unban user_id"
        )

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("Invalid User ID")

    await unban_user(user_id)

    await message.reply_text(
        f"✅ User `{user_id}` has been unbanned."
    )

    try:
        await client.send_message(
            user_id,
            "**🎉 You have been unbanned. You can use the bot again.**"
        )
    except:
        pass

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("banlist") & filters.private)
async def banlist(client, message):

    if message.from_user.id != OWNER_ID:
        return

    users = await get_banned_users()

    if not users:
        return await message.reply_text(
            "✅ No banned users."
        )

    text = "🚫 **Banned Users List**\n\n"

    for i, user in enumerate(users, 1):
        text += f"**{i}.** `{user}`\n"

    await message.reply_photo(
        photo="https://graph.org/file/26cccf142db47cbcc489e-5d5b36c222d0b2d898.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("addfsub") & filters.private)
async def add_fsub(client, message):

    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text("ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!")

    # Reply to forwarded channel post
    if message.reply_to_message:

        reply = message.reply_to_message

        if reply.forward_from_chat:
            chat = reply.forward_from_chat

        elif reply.sender_chat:
            chat = reply.sender_chat

        else:
            return await message.reply_text(
                "‼️ Reply to a forwarded channel post."
            )

        channel = chat.id

        # Username / ID method
    else:

        if len(message.command) < 2:
            return await message.reply_text(
                "Usage: /addfsub @channel\n"
                 "/addfsub -100xxxxxxxxxx\n\n"
                 "OR reply to a forwarded channel post with /addfsub."
            )

        channel = message.command[1]

        try:
            channel = int(channel)
        except:
            channel = channel.replace("@", "")

    try:
        chat = await client.get_chat(channel)

        me = await client.get_me()

        member = await client.get_chat_member(chat.id, me.id)

        if member.status not in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            return await message.reply_text(
                "‼️ 𝖥𝗂𝗋𝗌𝗍 𝗆𝖺𝗄𝖾 𝗆𝖾 𝖠𝖽𝗆𝗂𝗇 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅."
            )

    except Exception as e:
        return await message.reply_text(
            f"‼️ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝖺𝗇𝗇𝖾𝗅.\n\n{e}"
        )
    channels = await get_force_subs()

    if str(chat.id) in channels:
        return await message.reply_text(
            "**🧐 Tʜɪs Cʜᴀɴɴᴇʟ Is Aʟʀᴇᴀᴅʏ Iɴ Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ**"
        )
    
    if chat.username and chat.username in channels:
        return await message.reply_text(
            "**🧐 Tʜɪs Cʜᴀɴɴᴇʟ Is Aʟʀᴇᴀᴅʏ Iɴ Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ.**"
        )

    await add_force_sub(chat.id)

    await message.reply_text(
        f"**Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Aᴅᴅᴇᴅ**\n\n"
        f"**ᴄʜᴀɴɴᴇʟ:** {chat.title}\n"
        f"*ɪᴅ:** `{chat.id}`"
    )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("removefsub") & filters.private)
async def remove_fsub(client, message):

    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text("ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!.")

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n"
            "/removefsub @channel\n"
            "/removefsub -100xxxxxxxxxx"
        )

    channel = message.command[1]

    try:
        channel = int(channel)
    except:
        channel = channel.replace("@", "")

    try:
        chat = await client.get_chat(channel)

        await remove_force_sub(chat.id)

        if chat.username:
            await remove_force_sub(chat.username)
            await remove_force_sub(f"@{chat.username}")

        await message.reply_text(
            f"✅ Removed **{chat.title}** from Force Subscribe."
        )

    except Exception as e:
        return await message.reply_text(
            f"❌ Failed to remove.\n\n{e}"
        )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("fsublist") & filters.private)
async def fsub_list(client, message):

    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text("ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!")

    channels = await get_force_subs()

    if not channels:
        return await message.reply_text(
            "‼️ Nᴏ Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Cʜᴀɴɴᴇʟs ᴀᴅᴅᴇᴅ ᴏʀ Nᴏᴛ Fᴏᴜɴᴅ."
        )

    text = "**📢 Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Cʜᴀɴɴᴇʟs Lɪsᴛ**\n\n"

    for i, ch in enumerate(channels, start=1):
        try:
            chat = await client.get_chat(ch)

            if chat.username:
                text += f"**{i}.** @{chat.username}\n"
            else:
                text += (
                    f"**{i}.** {chat.title}\n"
                    f"**ID:** `{chat.id}`\n\n"
                )

        except:
            if str(ch).startswith("-100"):
                text += (
                    f"**{i}.** 🔒 Private Channel\n"
                    f"**ID:** `{ch}`\n\n"
                )
            else:
                text += f"**{i}.** @{ch}\n"

    await message.reply_photo(
        photo="https://graph.org/file/ffdbc01d09855874311b1-5f3f1eae52d984db3d.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")
                ]
            ]
        )
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ------------------------- #
# INDEX BACK CALLBACK
# ------------------------- #

@app.on_callback_query(filters.regex("^index_back$"))
async def index_back_callback(client, query):

    rows = []

    for i in range(0, 26, 4):
        row = []

        for letter in LETTERS[i:i+4]:
            row.append(
                InlineKeyboardButton(
                    letter,
                    callback_data=f"index_{letter}"
                )
            )

        rows.append(row)

    rows.append(
        [
            InlineKeyboardButton(
                "• ᴄʟᴏsᴇ •",
                callback_data="close"
            )
        ]
    )

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=INDEX_IMAGE,
            caption=(
                "**Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Iɴᴅᴇx**\n\n"
                "**Sᴇʟᴇᴄᴛ ᴀ ʟᴇᴛᴛᴇʀ ᴛᴏ ᴠɪᴇᴡ ᴄʜᴀɴɴᴇʟs**."
            )
        ),
        reply_markup=InlineKeyboardMarkup(rows)
    )

# ------------------------- #
# FORCE SUB CALLBACK
# ------------------------- #

    # ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_callback_query(filters.regex("checksub"))
async def checksub_callback(client, query):

    ok, keyboard = await check_force_sub(
        client,
        query.from_user.id
    )

    if not ok:
        return await query.answer(
            "‼️ Jᴏɪɴ ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs ғɪʀsᴛ.",
            show_alert=True
        )

    # animation
    await query.message.edit_media(
        InputMediaPhoto(
            CHECKING_IMAGE,
            "Cʜᴇᴄᴋɪɴɢ Sᴜʙsᴄʀɪᴘᴛɪᴏɴ..."
        )
    )

    await asyncio.sleep(1)

    await query.message.edit_caption("!")

    await asyncio.sleep(0.5)

    await query.message.edit_caption("!!")

    await asyncio.sleep(0.5)

    await query.message.edit_caption("!!!")

    await asyncio.sleep(0.5)

    param = await get_verify(query.from_user.id)

    if not param:
        return await query.answer(
            "**‼️ Vᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇxᴘɪʀᴇᴅ. Gᴏ Bᴀᴄᴋ ᴀɴᴅ Tʀʏ Aɢᴀɪɴ..**",
            show_alert=True
        )

    # remove force subscribe message
    await query.message.delete()

    # directly run start
    fake = type("obj", (), {})()

    fake.from_user = query.from_user
    fake.command = ["start", param]
    fake.text = f"/start {param}"
    fake.chat = query.message.chat

    fake.reply_text = query.message.reply_text
    fake.reply_photo = query.message.reply_photo
    fake.reply_video = query.message.reply_video
    fake.reply_audio = query.message.reply_audio
    fake.reply_document = query.message.reply_document
    fake.reply_animation = query.message.reply_animation
    fake.reply_sticker = query.message.reply_sticker
    fake.reply = query.message.reply_text

    await start(client, fake)
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
        
# ABOUT HANDLER
@app.on_callback_query(filters.regex("about"))
async def about_callback(client, query):
    await query.message.edit_text(
        "⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟\n\n"
        "‣ ᴍʏ ɴᴀᴍᴇ : [ᴀᴇʀᴏ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ](https://t.me/Aero_FileStoreBot)\n"
        "‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ᴍᴏʜᴀᴍᴍᴇᴅ](https://t.me/Mr_Mohammed_29)\n"
        "‣ ʟɪʙʀᴀʀʏ : [ᴘʏʀᴏɢʀᴀᴍ 𝟸.𝟶](https://pypi.org/project/Pyrogram/)\n"
        "‣ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ 𝟹](https://www.python.org/downloads/)\n"
        "‣ ᴅᴀᴛᴀ ʙᴀsᴇ : [ᴍᴏɴɢᴏ ᴅʙ](https://www.mongodb.com/)\n"
        "‣ ʙᴏᴛ sᴇʀᴠᴇʀ : [Bᴏᴛs Sᴇʀᴠᴇʀ](https://render.com)\n"
        "‣ ᴜᴘᴅᴀᴛᴇs : [ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs](https://t.me/Aero_Unity)\n"
        "‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ3.𝟶 [sᴛᴀʙʟᴇ](https://t.me/Aero_Unity)",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="home")]]
        ),
        parse_mode=ParseMode.MARKDOWN
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# HOME HANDLER
@app.on_callback_query(filters.regex("home"))
async def home_callback(client, query):

    photo = random.choice(IMAGES)

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=photo,
            caption=(
                "𝗛𝗲𝗹𝗹𝗼 ♡,\n\n"
                "›› 𝗜 𝗰𝗮𝗻 𝘀𝘁𝗼𝗿𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝗦𝗽𝗲𝗰𝗶𝗳𝗶𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝗼𝘁𝗵𝗲𝗿 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗮𝗰𝗰𝘀𝘀 𝗶𝘁 𝗳𝗿𝗼𝗺 𝘀𝗽𝗲𝗰𝗶𝗮𝗹 𝗹𝗶𝗻𝗸."
            ),
            parse_mode=ParseMode.MARKDOWN
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity"),
                    InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="about")
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/Mr_Mohammed_29")
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_callback_query(filters.regex("^close$"))
async def close_button(client, query):
    await query.message.delete()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# REFRESH STATS 
@app.on_callback_query(filters.regex("refresh_stats"))
async def refresh_stats(client, query):

    start = time.time()

    total = await total_users()
    total_files_count = await total_files()
    single_links, batch_links = await get_link_stats()

    uptime_seconds = int(time.time() - START_TIME)
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    ping = round((time.time() - start) * 1000, 3)

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    def progress(percent):
        filled = int(percent // 10)
        return "■" * filled + "▤" + "□" * (9 - filled)

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ", callback_data="refresh_stats")]
        ]
    )

    await query.message.edit_text(
        f"""⌬ <b>𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗜𝗦𝗧𝗜𝗖𝗦 :</b>

┎ <b>Bᴏᴛ Uᴘᴛɪᴍᴇ :</b> {hours}h {minutes}m {seconds}s
┃ <b>Cᴜʀʀᴇɴᴛ Pɪɴɢ :</b> {ping} ms
┖ <b>Tᴏᴛᴀʟ Uꜱᴇʀꜱ :</b> {total}

┎ <b>RAM ( MEMORY ) :</b>
┖ [{progress(ram.percent)}] {ram.percent}%

┎ <b>CPU ( USAGE ) :</b>
┖ [{progress(cpu)}] {cpu}%

┎ <b>DISK :</b>
┃ [{progress(disk.percent)}] {disk.percent}%
┃ <b>Usᴇᴅ :</b> {disk.used / (1024**3):.2f} GB
┃ <b>Fʀᴇᴇ :</b> {disk.free / (1024**3):.2f} GB
┖ <b>Tᴏᴛᴀʟ :</b> {disk.total / (1024**3):.2f} GB

┎ <b>Fɪʟᴇ Sᴛᴏʀᴇ :</b>
┃ <b>Tᴏᴛᴀʟ Fɪʟᴇs :</b> {total_files_count}
┃ <b>Sɪɴɢʟᴇ Lɪɴᴋs :</b> {single_links}
┖ <b>Bᴀᴛᴄʜ Lɪɴᴋs :</b> {batch_links}
""",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )

    await query.answer("Sᴛᴀᴛs Uᴘᴅᴀᴛᴇᴅ 🔄")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ------------------------- #
# ALIVE COMMAND
# ------------------------- #

@app.on_message(filters.command("alive"))
async def alive(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "🚫 **You are banned from using this bot.**"
        )

    await message.reply_photo(
        photo="https://graph.org/file/af61bc94f516c210ecb37-7cdb22e66ea9539e3b.jpg",
        caption=(
            "❤️ **Yᴏᴜ ᴀʀᴇ ᴠᴇʀʏ ʟᴜᴄᴋʏ 🤞 I ᴀᴍ ᴀʟɪᴠᴇ ❤️\n\n"
            "Pʀᴇss /start ᴛᴏ ᴜsᴇ ᴍᴇ!**"
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ------------------------- #
# ID COMMAND
# ------------------------- #

@app.on_message(filters.command("id"))
async def get_id(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "🚫 **You are banned from using this bot**"
        )

    user = message.from_user

    text = (
        "👤 **Usᴇʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ**\n\n"
        f"➲ **Fɪʀsᴛ Nᴀᴍᴇ**: {user.first_name or 'None'}\n"
        f"➲ **Lᴀsᴛ Nᴀᴍᴇ**: {user.last_name or 'None'}\n"
        f"➲ **Usᴇʀɴᴀᴍᴇ**: {user.username or 'None'}\n"
        f"➲ **Tᴇʟᴇɢʀᴀᴍ ID**: {user.id}\n"
        f"➲ **Dᴀᴛᴀ Cᴇɴᴛʀᴇ**: {user.dc_id or 'Unknown'}"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "👤 Vɪᴇᴡ Pʀᴏғɪʟᴇ",
                    url=f"https://t.me/{user.username}" if user.username else f"tg://openmessage?user_id={user.id}"
                )
            ]
        ]
    )

    try:
        photos = await client.get_profile_photos(
            user.id,
            limit=1
        )

        if photos:
            await message.reply_photo(
                photos[0].file_id,
                caption=text,
                reply_markup=keyboard
            )
        else:
            await message.reply_text(
                text,
                reply_markup=keyboard
            )

    except:
        await message.reply_text(
            text,
            reply_markup=keyboard
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("system"))
async def system_info(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "**🚫 You are banned from using this bot.**"
        )

    os_name = platform.system()

    uptime = int(time.time() - START_TIME)
    d, rem = divmod(uptime, 86400)
    h, rem = divmod(rem, 3600)
    m, s = divmod(rem, 60)

    sys_time = int(time.time() - psutil.boot_time())
    sd, rem = divmod(sys_time, 86400)
    sh, rem = divmod(rem, 3600)
    sm, ss = divmod(rem, 60)

    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    text = (
        "💻 **Sʏsᴛᴇᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Pᴀɴᴇʟ**\n\n"
        f"🖥️ **OS Dᴇᴛᴀɪʟs** : {os_name}\n"
        f"⏰ **Bᴏᴛ Uᴘᴛɪᴍᴇ** : {d}ᴅ : {h}ʜ : {m}ᴍ : {s}s\n"
        f"🔄 **Sʏsᴛᴇᴍ Uᴘᴛɪᴍᴇ** : {sd}ᴅ : {sh}ʜ : {sm}ᴍ : {ss}s\n"
        f"💾 **Rᴀᴍ Usᴀɢᴇ** : {ram.used/(1024**3):.2f} GB / {ram.total/(1024**3):.2f} GB\n"
        f"📁 **Dɪsᴋ Usᴀɢᴇ** : {disk.used/(1024**3):.2f} GB / {disk.total/(1024**3):.2f} GB"
    )

    await message.reply_photo(
        photo="https://graph.org/file/3999f429ad9b0b1317f28-7591e7676c147975c9.jpg",
        caption=text
    )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("restart") & filters.private)
async def restart_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
        )

    text = (
        "<blockquote>🔄 <b>Bᴏᴛ Rᴇsᴛᴀʀ</b></blockquote>\n\n"
        "• <b>Status:</b> Rᴇsᴛᴀʀᴛɪɴɢ Bᴏᴛ..\n"
        "<blockquote>⚡ All services will automatically reconnect after restart.</blockquote>"
    )

    await message.reply_photo(
        photo="https://graph.org/file/14c3a336058422b14549d-85d887f6fd8a9cead5.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")]]
        )
    )

    os.execl(sys.executable, sys.executable, *sys.argv)

# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #

DISCLAIMER_TEXT = """
<blockquote><b>ᴅɪsᴄʟᴀɪᴍᴇʀ</b></blockquote>

• Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ Aᴇʀᴏ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.

• Pʟᴇᴀsᴇ ʀᴇᴀᴅ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʙᴇғᴏʀᴇ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ.

○ Cʜᴏᴏsᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ:

• 🔒 Pʀɪᴠᴀᴄʏ Pᴏʟɪᴄʏ
• 🚀 Vᴇʀsɪᴏɴ Iɴғᴏʀᴍᴀᴛɪᴏɴ
• 🛠 Sᴜᴘᴘᴏʀᴛ Cᴇɴᴛᴇʀ
"""

PRIVACY_TEXT = """
<blockquote><b>🔒 ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ</b></blockquote>

•Yᴏᴜʀ ᴘʀɪᴠᴀᴄʏ ɪs ɪᴍᴘᴏʀᴛᴀɴᴛ ᴛᴏ ᴜs.

<b>📂 Dᴀᴛᴀ Wᴇ sᴛᴏʀe</b>
• Tᴇʟᴇɢʀᴀᴍ Usᴇʀ ID
• Uᴘʟᴏᴀᴅᴇᴅ Fɪʟᴇ IDs
• Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Sᴛᴀᴛᴜs

<b>❌ Dᴀᴛᴀ Wᴇ Nᴇᴠᴇʀ Sᴛᴏʀᴇs</b>
• Fɪʟᴇɴᴀᴍᴇs ᴀɴᴅ ᴄᴀᴘᴛɪᴏɴs
• Pᴀssᴡᴏʀᴅs
• Pʜᴏɴᴇ Nᴜᴍʙᴇʀs
• Pʀɪᴠᴀᴛᴇ Cʜᴀᴛs
• Pᴀʏᴍᴇɴᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ

<b>🔐 sᴇᴄᴜʀɪᴛʏ</b>

• Aʟʟ ᴅᴀᴛᴀ ɪs sᴇᴄᴜʀᴇʟʏ sᴛᴏʀᴇᴅ ᴀɴᴅ ɪs ɴᴇᴠᴇʀ sʜᴀʀᴇᴅ ᴡɪᴛʜ ᴛʜɪʀᴅ ᴘᴀʀᴛɪᴇs.
"""

VERSION_TEXT = f"""
<blockquote><b>ʙᴏᴛ ᴠᴇʀsɪᴏɴ</b></blockquote>

🤖 <b>ʙᴏᴛ ᴠᴇʀsɪᴏɴ</b> <code>{BOT_VERSION}</code>
🐍 <b>• Pʏᴛʜᴏɴ •</b> <code>𝟹.𝟷𝟷.𝟷𝟻</code>
⚡ <b>• Pʏʀᴏɢʀᴀᴍ •</b> <code>𝟸.𝟶.𝟷𝟶𝟼</code>
🗄  <b>• Dᴀᴛᴀʙᴀsᴇ •</b> <code>MᴏɴɢᴏDB Aᴛʟᴀs</code>
🌐 <b>• Hᴏsᴛɪɴɢ •</b> <code>Rᴇɴᴅᴇʀ Wᴇʙ Sᴇʀᴠɪᴄᴇ</code>
👨‍💻 <b>• Dᴇᴠᴇʟᴏᴘᴇʀ •</b> <a href="https://t.me/Mr_Mohammed_29">Mᴏʜᴀᴍᴍᴇᴅ</a>
📢 <b>• ᴜᴘᴅᴀᴛᴇs •</b> <a href="https://t.me/Aero_Unity">Aᴇʀᴏ Uɴɪᴛʏ</a>
💬 <b>• sᴜᴘᴘᴏʀᴛ •</b> <a href="https://t.me/+KWvhNb8kkmExNDc1">Discussion</a>
🌟 <b>• Gɪᴛʜᴜʙ •</b> <a href="https://github.com/MohammedDev-yt">Cʟɪᴄᴋ Hᴇʀᴇ</a>
"""

SUPPORT_TEXT = """
<blockquote><b>sᴜᴘᴘᴏʀᴛ</b></blockquote>

• Bᴏᴛ Issᴜᴇs
• Dᴀᴛᴀʙᴀsᴇ Pʀᴏʙʟᴇᴍs
• Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Hᴇʟᴘ
• Dᴇᴘʟᴏʏᴍᴇɴᴛ Sᴜᴘᴘᴏʀᴛ
• Fᴇᴀᴛᴜʀᴇ Rᴇǫᴜᴇsᴛs
• Bᴜɢ Rᴇᴘᴏʀᴛs

<blockquote>
📨 𝖯𝗅𝖾𝖺𝗌𝖾 𝖽𝖾𝗌𝖼𝗋𝗂𝖻𝖾 𝗒𝗈𝗎𝗋 𝗂𝗌𝗌𝗎𝖾 𝖼𝗅𝖾𝖺𝗋𝗅𝗒.
𝖱𝖾𝗌𝗉𝗈𝗇𝗌𝖾 𝗍𝗂𝗆𝖾 𝗂𝗌 𝗎𝗌𝗎𝖺𝗅𝗅𝗒 𝗐𝗂𝗍𝗁𝗂𝗇 𝖺 𝖿𝖾𝗐 𝗁𝗈𝗎𝗋𝗌.
</blockquote>
"""

@app.on_message(filters.command("disclaimer") & filters.private)
async def disclaimer_cmd(client, message):

    await message.reply_photo(
        photo="https://graph.org/file/186013fea801dbb851bbd-8df16c2f5040ac02c7.jpg",
        caption=DISCLAIMER_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴘʀɪᴠᴀᴄʏ •",
                        callback_data="privacy_page"
                    ),
                    InlineKeyboardButton(
                        "• ᴠᴇʀsɪᴏɴ •",
                        callback_data="version_page"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• sᴜᴘᴘᴏʀᴛ •",
                        callback_data="support_page"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

# ------------------------- #
# Privacy Page
# ------------------------- #

@app.on_callback_query(filters.regex("^privacy_page$"))
async def privacy_page(client, query):

    await query.message.edit_caption(
        caption=PRIVACY_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ʙᴀᴄᴋ •",
                        callback_data="disclaimer_home"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

    await query.answer()

# ------------------------- #
# Version Page
# ------------------------- #

@app.on_callback_query(filters.regex("^version_page$"))
async def version_page(client, query):

    await query.message.edit_caption(
        caption=VERSION_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ʙᴀᴄᴋ •",
                        callback_data="disclaimer_home"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

    await query.answer()

# ------------------------- #
# Support Page
# ------------------------- #

@app.on_callback_query(filters.regex("^support_page$"))
async def support_page(client, query):

    await query.message.edit_caption(
        caption=SUPPORT_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴅᴇᴠᴇʟᴏᴘᴇʀ •",
                        url="https://t.me/Mr_Mohammed_29"
                    ),
                    InlineKeyboardButton(
                        "• sᴜᴘᴘᴏʀᴛ •",
                        url="https://t.me/+KWvhNb8kkmExNDc1"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴜᴘᴅᴀᴛᴇs •",
                        url="https://t.me/Aero_Unity"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ʙᴀᴄᴋ •",
                        callback_data="disclaimer_home"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

    await query.answer()

# ------------------------- #
# Disclaimer Home
# ------------------------- #

@app.on_callback_query(filters.regex("^disclaimer_home$"))
async def disclaimer_home(client, query):

    await query.message.edit_caption(
        caption=DISCLAIMER_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴘʀɪᴠᴀᴄʏ •",
                        callback_data="privacy_page"
                    ),
                    InlineKeyboardButton(
                        "• ᴠᴇʀsɪᴏɴ •",
                        callback_data="version_page"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• sᴜᴘᴘᴏʀᴛ •",
                        callback_data="support_page"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

    await query.answer()
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("speedtest") & filters.private)
async def speedtest_cmd(client, message):

    msg = await message.reply_text(
        "⚡ Rᴜɴɴɪɴɢ Iɴᴛᴇʀɴᴇᴛ Sᴘᴇᴇᴅ Tᴇsᴛ...\n"
        "Tʜɪs Mᴀʏ Tᴀᴋᴇ 𝟷𝟶 - 𝟸𝟶 sᴇᴄ........"
    )

    try:
        start = time.time()

        st = speedtest.Speedtest()

        st.get_best_server()

        download = st.download() / 1024 / 1024
        upload = st.upload() / 1024 / 1024

        ping = st.results.ping

        elapsed = round(time.time() - start, 2)

        await msg.delete()

        caption = f"""
<blockquote><b>Sᴘᴇᴇᴅ Tᴇxᴛ Rᴇsᴜʟᴛ</b></blockquote>

📡 <b>Sᴇʀᴠᴇʀ :</b> <code>{st.results.server['sponsor']}</code>
🌍 <b>Cᴏᴜɴᴛʀʏ :</b> <code>{st.results.server['country']}</code>
📥 <b>Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{download:.2f} Mbps</code>
📤 <b>Uᴘʟᴏᴀᴅ :</b> <code>{upload:.2f} Mbps</code>
📶 <b>Pɪɴɢ :</b> <code>{ping:.2f} ms</code>
⏱ <b>Tɪᴍᴇ Tᴀᴋᴇɴ :</b> <code>{elapsed} sec</code>

• <b>Nᴇᴛᴡᴏʀᴋ Sᴘᴇᴇᴅ Tᴇxᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ.</b>
"""

        await message.reply_photo(
            photo="https://graph.org/file/24b1d71722e3272349f71-dc01805818fa2e8c67.jpg",
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

    except Exception as e:
        await msg.edit(
            f"😢 Sᴘᴇᴇᴅ ᴛᴇsᴛ ғᴀɪʟᴇᴅ\n\n<code>{e}</code>"
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("adddb") & filters.private)
async def adddb_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
        )

    if len(message.command) < 3:
        return await message.reply_text(
            "<b>Usage:</b>\n"
            "<code>/adddb 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾𝖭𝖺𝗆𝖾 𝗆𝗈𝗇𝗀𝗈𝖽𝖻+srv://.....</code>"
        )

    if total_databases() >= 5:
        return await message.reply_text(
            "🤧 <b>Mᴀxɪᴍᴜᴍ 𝟻 Dᴀᴛᴀʙᴀsᴇ Wɪʟʟ Bᴇ Aʟʟᴏᴡᴇᴅ.</b>"
        )

    name = message.command[1]

    uri = message.text.split(None, 2)[2]

    dbs = await get_all_databases()

    for db in dbs:

        if db["name"].lower() == name.lower():

            return await message.reply_text(
                "⚠️ <b>Dᴀᴛᴀʙᴀsᴇ Nᴀᴍᴇ Aʟʀᴇᴀᴅʏ Exɪᴛs , Pʟᴇᴀsᴇ Gɪᴠᴇ Aɴᴏᴛʜᴇʀ Nᴀᴍᴇ.</b>"
            )

    wait = await message.reply_text(
        "🔄 <b>Cᴏɴɴᴇᴄᴛɪɴɢ Tᴏ MᴏɴɢᴏDB...</b>"
    )

    try:

        await load_database(uri, name)

        await add_database(name, uri)

        await wait.delete()

        await message.reply_photo(
            photo="https://graph.org/file/cb707ebcf6e087d4a49c6-ce0dbf8bc97b6dd50b.jpg",
            caption=f"""
<blockquote><b>✅ Dᴀᴛᴀʙᴀsᴇ Cᴏɴɴᴇᴄᴛᴇᴅ</b></blockquote>

○ <b>ɴᴀᴍᴇ</b> <code>{name}</code>
○ <b>sᴛᴀᴛᴜs</b> Cᴏɴɴᴇᴄᴛᴇᴅ [ Aʟɪᴠᴇ ]
<blockquote><b>🔄 It will automatically reconnect after every bot restart.</b></blockquote>
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

    except Exception as e:

        await wait.edit(
            f"🔗 <b>Cᴏɴɴᴇᴄᴛɪᴏɴ Fᴀɪʟᴇᴅ</b>\n\n<code>{e}</code>"
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("removedb") & filters.private)
async def removedb_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
        )

    if len(message.command) != 2:
        return await message.reply_text(
            "<b>Usage:</b>\n"
            "<code>/removedb DᴀᴛᴀʙᴀsᴇNᴀᴍᴇ</code>"
        )

    db_name = message.command[1]

    if not has_database(db_name):
        return await message.reply_text(
            "‼️ <b>Dᴀᴛᴀʙᴀsᴇ ɴᴏᴛ ғᴏᴜɴᴅ.</b>"
        )

    current = get_active_database()

    wait = await message.reply_text(
        "🗑 ʀᴇᴍᴏᴠɪɴɢ ᴅᴀᴛᴀʙᴀsᴇ..."
    )

    try:

        await remove_loaded_db(db_name)

        await remove_saved_db(db_name)

        dbs = database_list()

        extra = ""

        if current == db_name:

            if dbs:

                new_db = dbs[0]

                switch_database(new_db)

                await set_active_database(new_db)

                extra = (
                    f"\n\n<b>ɴᴇᴡ ᴀᴄᴛɪᴠᴇ ᴅᴀᴛᴀʙᴀsᴇ :</b>\n"
                    f"<code>{new_db}</code>"
                )

            else:

                extra = "\n\n⚠️ Nᴏ ᴅᴀᴛᴀʙᴀsᴇs ʀᴇᴍᴀɪɴɪɴɢ..."

        await wait.delete()

        await message.reply_photo(
            photo="https://graph.org/file/cb707ebcf6e087d4a49c6-ce0dbf8bc97b6dd50b.jpg",
            caption=f"""
<blockquote><b>Dᴀᴛᴀʙᴀsᴇ Rᴇᴍᴏᴠᴇᴅ</b></blockquote>

🗄 <b>Dᴀᴛᴀʙᴀsᴇ :</b> <code>{db_name}</code>
✅ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ. {extra}
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

    except Exception as e:

        await wait.edit(
            f"❌ <b>Failed</b>\n\n<code>{e}</code>"
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("dblist") & filters.private)
async def dblist_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
        )

    wait = await message.reply_text(
        "🔎 Fᴇᴛᴄʜɪɴɢ Dᴀᴛᴀʙᴀsᴇ Lɪsᴛ..."
    )

    try:

        dbs = await database_status()

        if not dbs:

            await wait.edit(
                "‼️ Nᴏ Dᴀᴛᴀʙᴀsᴇs Aᴅᴅᴇᴅ ᴏʀ ғᴏᴜɴᴅ.</b>"
            )

            return

        active = get_active_database()

        online = 0
        offline = 0

        text = """
<blockquote><b>Dᴀᴛᴀʙᴀsᴇ Lɪsᴛ</b></blockquote>

"""

        for i, db in enumerate(dbs, start=1):

            if db["status"] == "ONLINE":

                status = "○ ᴏɴʟɪɴᴇ"

                online += 1

            else:

                status = "○ ᴏғғʟɪɴᴇ"

                offline += 1

            current = ""

            if db["name"] == active:

                current = "○ ᴀᴄᴛɪᴠᴇ"

            text += (
                f"<b>{i}.</b> <code>{db['name']}</code>\n"
                f"Status : {status}{current}\n\n"
            )
        text += f"""
<blockquote>
○ ᴏɴʟɪɴᴇ : {online}
○ ᴏғғʟɪɴᴇ : {offline}
○ Tᴏᴛᴀʟ Dᴀᴛᴀʙᴀsᴇs : {len(dbs)}/5
</blockquote>
"""

        await wait.delete()

        await message.reply_photo(
            photo="https://graph.org/file/cb707ebcf6e087d4a49c6-ce0dbf8bc97b6dd50b.jpg",
            caption=text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

    except Exception as e:

        await wait.edit(
            f"❌ <b>Error</b>\n\n<code>{e}</code>"
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("dbstatus") & filters.private)
async def dbstatus_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
        )

    wait = await message.reply_text(
        "🔎 ᴄʜᴇᴄᴋɪɴɢ ᴅᴀᴛᴀʙᴀsᴇ sᴛᴀᴛᴜs..."
    )

    try:

        dbs = await database_status()

        if not dbs:
            return await wait.edit(
                "‼️ Nᴏ Dᴀᴛᴀʙᴀsᴇs Aᴅᴅᴇᴅ."
            )

        active = get_active_database()

        online = 0
        offline = 0

        caption = """
<blockquote><b>ᴅᴀᴛᴀʙᴀsᴇ sᴛᴀᴛᴜs</b></blockquote>

"""
        for i, db in enumerate(dbs, start=1):

            if db["status"] == "ᴏɴʟɪɴᴇ":
                status = "○ ᴏɴʟɪɴᴇ"
                online += 1
            else:
                status = "○ ᴏғғʟɪɴᴇ"
                offline += 1

            active_text = ""

            if db["name"] == active:
                active_text = "○ ᴀᴄᴛɪᴠᴇ"

            caption += (
                f"🗄 <b>Dᴀᴛᴀʙᴀsᴇ {i}</b>\n"
                f"├ <b>Dᴀᴛᴀʙᴀsᴇ Nᴀᴍᴇ :</b> <code>{db['name']}</code>\n"
                f"└ <b>Sᴛᴀᴛᴜs :</b> {status}{active_text}\n"
            )
        caption += f"""
<blockquote>
○ ᴏɴʟɪɴᴇ : <code>{online}</code>
○ ᴏғғʟɪɴᴇ : <code>{offline}</code>
○ Tᴏᴛᴀʟ Dᴀᴛᴀʙᴀsᴇs : <code>{len(dbs)}/5</code>
○ Aᴄᴛɪᴠᴇ Dᴀᴛᴀʙᴀsᴇ : <code>{active if active else 'None'}</code>
</blockquote>
"""
        await wait.delete()

        await message.reply_photo(
            photo="https://graph.org/file/cb707ebcf6e087d4a49c6-ce0dbf8bc97b6dd50b.jpg",
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

    except Exception as e:

        await wait.edit(
            f"❌ <b>Error</b>\n\n<code>{e}</code>"
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("lyrics"))
async def lyrics_cmd(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            """
<blockquote expandable>

🎵 <b>ʜᴏᴡ ᴛᴏ sᴇᴀʀᴄʜ sᴏɴɢ ʟʏʀɪᴄs</b>

<b>Usage:</b>
<code>/lyrics Believer</code>
<code>/lyrics Sahiba</code>

</blockquote>
"""
        )

    query = " ".join(message.command[1:])

    msg = await message.reply_text("🔍 Sᴇᴀʀᴄʜɪɴɢ Lʏʀɪᴄs...")

    lyrics = get_lyrics(query)

    if not lyrics:
        return await msg.edit(
            """
<blockquote expandable>

‼️ <b>Lʏʀɪᴄs Nᴏᴛ Fᴏᴜɴᴅ.</b>

• Cʜᴇᴄᴋ Oᴜᴛ Fʀᴏᴍ Gᴏᴏɢʟᴇ ᴏʀ Sᴘᴇʟʟɪɴɢ ᴀɴᴅ Tʀʏ Aɢᴀɪɴ.

</blockquote>
"""
        )

    pages = split_lyrics(lyrics)

    user_id = message.from_user.id

    LYRICS_CACHE[user_id] = {
        "pages": pages,
        "song": query
    }

    text = f"""
<blockquote expandable>

🎵 <b>{query.title()}</b> 

{pages[0]}

</blockquote>

<b>Page 1/{len(pages)}</b>
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="lyrics_close"),
                InlineKeyboardButton("• ɴᴇxᴛ •", callback_data="lyrics_next_0")
            ]
        ]
    )

    await msg.edit(
        text,
        reply_markup=buttons
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_callback_query(filters.regex(r"^lyrics_(next|back|close)"))
async def lyrics_buttons(client, query: CallbackQuery):

    if query.data == "lyrics_close":
        await query.message.delete()
        return await query.answer()

    user_id = query.from_user.id

    if user_id not in LYRICS_CACHE:
        return await query.answer("Lʏʀɪᴄs Gᴇɴᴇʀᴀᴛᴇ Fᴀɪʟᴇᴅ, Cᴏɴᴛᴀᴄᴛ Tᴏ Oᴡɴᴇʀ [ @Mr_Mohammed_29]", show_alert=True)

    data = LYRICS_CACHE[user_id]
    pages = data["pages"]
    song = data["song"]

    page = int(query.data.split("_")[-1])

    if "next" in query.data:
        page += 1
    elif "back" in query.data:
        page -= 1

    if page < 0:
        page = 0

    if page >= len(pages):
        page = len(pages) - 1

    text = f"""
<blockquote expandable>

🎵 <b>{song.title()}</b> 

{pages[page]}

</blockquote>

<b>Page {page+1}/{len(pages)}</b>
"""

    buttons = []

    row = []

    if page > 0:
        row.append(
            InlineKeyboardButton(
                "• ʙᴀᴄᴋ •",
                callback_data=f"lyrics_back_{page}"
            )
        )

    row.append(
        InlineKeyboardButton(
            "• ᴄʟᴏsᴇ •",
            callback_data="lyrics_close"
        )
    )

    if page < len(pages) - 1:
        row.append(
            InlineKeyboardButton(
                "• ɴᴇxᴛ •",
                callback_data=f"lyrics_next_{page}"
            )
        )

    buttons.append(row)

    await query.message.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    await query.answer()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("translate"))
async def translate_cmd(client, message):
    if len(message.command) < 3:
        return await message.reply_text(
            "Usage:\n<code>/translate 𝖾𝗇 𝖧𝖾𝗅𝗅𝗈 𝖶𝗈𝗋𝗅𝖽</code>"
        )

    lang = message.command[1]
    text = " ".join(message.command[2:])

    try:
        translated = GoogleTranslator(source="auto", target=lang).translate(text)
        await message.reply_text(
            f"<blockquote expandable>\n"
            f"🌐<b>ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀᴀɴsʟᴀᴛɪᴏɴ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</b>\n\n"
            f"<b>ʟᴀɴɢᴜᴀɢᴇ:</b> {lang}\n"
            f"<b>ʀᴇsᴜʟᴛ:</b> <code>{translated}</code>\n"
            f"</blockquote>"
        )
    except Exception as e:
        await message.reply_text(f"❌ Error: <code>{e}</code>")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #      

async def restore_databases():
    dbs = await get_all_databases()

    for db in dbs:
        try:
            await load_database(
                db["mongo_uri"],
                db["name"]
            )
            print(f"Loaded DB: {db['name']}")
        except Exception as e:
            print(f"Failed to load {db['name']} -> {e}")

    active = await get_saved_active_database()

    if active:
        switch_database(active)

if __name__ == "__main__":
    keep_alive()  

    app.loop.run_until_complete(
        restore_databases()
    )
    print("""
╔══════════════════════════════╗
║   ᴍᴏʜᴀᴍᴍᴇᴅᴅᴇᴠ-ʏᴛ                   ║
║   ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ.            ║
╚══════════════════════════════╝
""")
    app.run()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #