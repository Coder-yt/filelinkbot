from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from database import ( save_file, get_file, add_user, get_all_users, total_users, add_admin, remove_admin, ban_user, unban_user, is_banned )
from pyrogram.handlers import MessageHandler
from keep_alive import keep_alive
import asyncio

app = Client(
    "filelinkbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
# 🚫 BAN CHECK (ADDED - DO NOT MODIFY OLD CODE)
# =========================
@app.on_message(filters.all)
async def ban_check(client, message):
    if message.from_user:
        if await is_banned(message.from_user.id):
            return await message.reply_text("🚫 You are banned from using this bot.")

app.add_handler(MessageHandler(ban_check, filters.all))
            
# START + LINK HANDLER
@app.on_message(filters.command("start"))
async def start(client, message: Message):
    user_id = message.from_user.id
    await add_user(message.from_user.id)

    # ✅ ADDED START ANIMATION
    m = await message.reply_text("ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻. . .")
    await asyncio.sleep(0.5)
    await m.edit_text("🎊")
    await asyncio.sleep(0.5)
    await m.edit_text("⚡")
    await asyncio.sleep(0.5)
    await m.edit_text("sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...")
    await asyncio.sleep(0.5)
    await m.delete()

    await message.reply_sticker("CAACAgUAAxkBAAEcODlp3ayV-H4JKd81Rbpm1LA3xNusNgACgx8AAvKI0FaRFZgCkrs1NB4E")

    if len(message.command) > 1:
        file_unique_id = message.command[1]
        data = await get_file(file_unique_id)

        if not data:
            return await message.reply_text("🔎 Fɪʟᴇ Is Nᴏᴛ Fᴏᴜɴᴅ, Cᴏɴᴛᴀᴄᴛ Tᴏ Oᴡɴᴇʀ.")

        original_caption = data.get("caption", "")
        caption = f"{original_caption}\n\n›› Cʜᴀɴɴᴇʟ : @Anime_UpdatesAU"

        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Anime_UpdatesAU")]]
        )

        if data.get("file_type") == "video":
            sent = await message.reply_video(
                data["file_id"],
                caption=caption,
                reply_markup=buttons
            )

        elif data.get("file_type") == "audio":
            sent = await message.reply_audio(
                data["file_id"],
                caption=caption,
                reply_markup=buttons
            )

        else:
            sent = await message.reply_document(
                data["file_id"],
                caption=caption,
                reply_markup=buttons
            )

        # ✅ ADDED AFTER FILE ANIMATION
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

        return

    # ✅ UPDATED START MESSAGE WITH BUTTONS
    await message.reply_text(
        "Hᴇʏ Wᴇʟᴄᴏᴍᴇ ᴛᴏ Oғғɪᴄɪᴀʟ @AU_Luffy_Store_bot\n\n›› Tʜɪs ʙᴏᴛ sᴛᴏʀᴇs ᴛʜᴇ ғɪʟᴇs ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ʟɪɴᴋs ᴛᴏ ᴛʜᴇ ᴏᴡɴᴇʀ ᴀɴᴅ ᴜsᴇʀ ᴄᴀɴ ᴀᴄᴄᴇss ғᴏʀ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ\n\n›› Oᴡɴᴇʀ : @Mr_Mohammed_29",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Anime_UpdatesAU")],
                [InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")]
            ]
        )
    )


# OWNER UPLOAD ONLY
@app.on_message(
    (filters.document | filters.video | filters.audio) &
    filters.user(OWNER_ID)
)
async def save_media(client, message: Message):

    original_caption = message.caption if message.caption else ""

    if message.video:
        file = message.video
        file_type = "video"
    elif message.audio:
        file = message.audio
        file_type = "audio"
    else:
        file = message.document
        file_type = "document"

    file_id = file.file_id
    file_unique_id = file.file_unique_id

    await save_file(file_id, file_unique_id, file_type, original_caption)

    link = f"https://t.me/{BOT_USERNAME}?start={file_unique_id}"

    await message.reply_text(f"🔗 𝗛𝗲𝗿𝗲 𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸:\n{link}")


# BLOCK OTHERS (UNCHANGED)
@app.on_message(
    (filters.document | filters.video | filters.audio) &
    ~filters.user(OWNER_ID)
)
async def block_users(client, message: Message):
    await message.reply_text("ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃..")


# STATS (UNCHANGED)
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(client, message: Message):
    total = await total_users()
    await message.reply_text(f"📊 Tᴏᴛᴀʟ Usᴇʀs: {total}")

# BROADCAST (UNCHANGED)
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message: Message):

    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to broadcast.")

    msg = message.reply_to_message

    users = await get_all_users()

    sent = 0
    failed = 0

    status = await message.reply_text("🚀 Broadcasting started...")  # ✅ INSIDE FUNCTION

    for user_id in users:
        try:
            await msg.copy(chat_id=int(user_id))
            sent += 1
            await asyncio.sleep(0.2)

        except Exception as e:
            failed += 1
            print(f"Failed: {user_id} | {e}")

    await status.edit_text(
        f"📢 Broadcast Complete\n\n"
        f"✅ Sent: {sent}\n"
        f"❌ Failed: {failed}"
    )

# =========================
# 👑 ADMIN SYSTEM (ADDED ONLY)
# =========================

@app.on_message(filters.command("addadmin") & filters.user(OWNER_ID))
async def addadmin(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /addadmin user_id")

    await add_admin(message.command[1])
    await message.reply_text("✅ Admin added")


@app.on_message(filters.command("deladmin") & filters.user(OWNER_ID))
async def deladmin(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /deladmin user_id")

    await remove_admin(message.command[1])
    await message.reply_text("❌ Admin removed")


@app.on_message(filters.command("ban") & filters.user(OWNER_ID))
async def ban(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /ban user_id")

    await ban_user(message.command[1])
    await message.reply_text("🚫 User banned")


@app.on_message(filters.command("unban") & filters.user(OWNER_ID))
async def unban(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /unban user_id")

    await unban_user(message.command[1])
    await message.reply_text("✅ User unbanned")


@app.on_message(filters.command("info") & filters.user(OWNER_ID))
async def info(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /info user_id")

    user_id = message.command[1]
    await message.reply_text(f"👤 User ID: {user_id}")

        
# ✅ ADDED ABOUT HANDLER
@app.on_callback_query(filters.regex("about"))
async def about_callback(client, query):
    await query.message.edit_text(
        "⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟\n\n‣ ᴍʏ ɴᴀᴍᴇ : @AU_Luffy_Store_bot\n‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : @Mr_Mohammed_29(ᴍᴏʜᴀᴍᴍᴇᴅ)\n‣ ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ\n‣ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3\n‣ ᴅᴀᴛᴀ ʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ\n‣ ʙᴏᴛ sᴇʀᴠᴇʀ : @BotsServerDead\n‣ᴜᴘᴅᴀᴛᴇs : @Anime_UpdatesAU\n‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : [sᴛᴀʙʟᴇ]",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        )
    )


# ✅ ADDED HOME HANDLER
@app.on_callback_query(filters.regex("home"))
async def home_callback(client, query):
    await query.message.edit_text(
        "Hᴇʏ Wᴇʟᴄᴏᴍᴇ ᴛᴏ Oғғɪᴄɪᴀʟ @AU_Luffy_Store_bot\n\n›› Tʜɪs ʙᴏᴛ sᴛᴏʀᴇs ᴛʜᴇ ғɪʟᴇs ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ʟɪɴᴋs ᴛᴏ ᴛʜᴇ ᴏᴡɴᴇʀ ᴀɴᴅ ᴜsᴇʀ ᴄᴀɴ ᴀᴄᴄᴇss ғᴏʀ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ\n\n›› Oᴡɴᴇʀ : @Mr_Mohammed_29",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Anime_UpdatesAU")],
                [InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")]
            ]
        )
    )


# RUN
keep_alive()
app.run()

#----Don't Remove Credit----# 
#----owner @Mr_Mohammed_29----# 
