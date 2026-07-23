
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=36BCF7F1&width=435&lines=Welcome+To+Adavance+File+Store+bot;Bot+is+Made+By+Mohammed)](https://git.io/typing-svg)

---

<p align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3"/>
  </a>
  <a href="https://docs.pyrogram.org/" target="_blank">
    <img src="https://img.shields.io/badge/Framework-Pyrogram-brightgreen?style=for-the-badge&logo=pyrogram&logoColor=white" alt="Pyrogram"/>
  </a>
  <a href="https://t.me/Mr_Mohammed_29" target="_blank">
    <img src="https://img.shields.io/badge/Developer-Mohammed-purple?style=for-the-badge&logo=telegram&logoColor=white" alt="Developer"/>
  </a>
  <a href="https://t.me/Aero_Unity" target="_blank">
    <img src="https://img.shields.io/badge/Support-Group-blueviolet?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group"/>
  </a>
</p>

## 🚀 Project Status

![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Telegram-blue)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)

# 🤖 File Store Bot

![Repo Size](https://img.shields.io/github/repo-size/Coder-yt/filelinkbot)
![Stars](https://img.shields.io/github/stars/Coder-yt/filelinkbot?style=social)
![Forks](https://img.shields.io/github/forks/Coder-yt/filelinkbot?style=social)
![Last Commit](https://img.shields.io/github/last-commit/Coder-yt/filelinkbot)

## ✨ Features

### 👤 User Features
- 🚀 **Start Bot** with Premium Home Interface
- 📦 **Batch File Store** for Telegram Channel Messages (Owner/Admin Uploads)
- 🔗 **Instant Shareable File Links**
- 🆔 **User ID** Lookup
- 💚 **Alive Check**
- ⚠️ **Disclaimer** Information
- 🌍 **Text Translation** into Multiple Languages
- 🎵 **Song Lyrics Search**
- 🌐 **Telegraph Links**
- 🖼️ **Premium UI** with Images & Inline Buttons

### 👑 Owner & Admin Features
- 📥 **Batch Indexing** of Telegram Channel Posts
- 📈 **Bot Statistics**
- 📑 **Force Subscribe Index**
- ➕ **Add Force Subscribe** Channels
- ➖ **Remove Force Subscribe** Channels
- 📋 **Force Subscribe List**
- ➕ **Add Admin**
- ➖ **Remove Admin**
- 👥 **Admin List**
- 🔨 **Ban Users**
- 🔓 **Unban Users**
- 🚫 **Banned Users List**
- 🔄 **Restart Bot**
- ➕ **Add MongoDB Database**
- ➖ **Remove MongoDB Database**
- 📋 **Database List**
- 🗄️ **Database Status**
- 📢 **Broadcast Messages** to All Users

### ⚙️ Technical Features
- 🚀 Built with **Pyrogram 2.x**
- 🗄️ **MongoDB (Motor)** Database
- ☁️ **Render Deployment Ready**
- ⚡ **Async & High-Speed Performance**
- 🔒 **Secure Force Subscribe System**
- 📂 **Unlimited File Storage**
- 📊 **Multi-Database Support**
- 🌐 **Telegraph Integration**
- 🎨 **Premium Command UI**
- 🖥️ **24/7 Uptime Support**

📂 Supported Media Types

- 🎥 Videos
- 📄 Documents
- 🎵 Audio Files
- 🖼 GIF / Animations
- 😄 Stickers

## ⚙️ Configuration Variables

| Variable        | Description                                  | Example / Format              |
|----------------|----------------------------------------------|-------------------------------|
| API_ID         | Your Telegram API ID                         | 123456                        |
| API_HASH       | Your Telegram API Hash                       | abcdef1234567890abcdef       |
| BOT_TOKEN      | Bot token from BotFather                     | 123456:ABC-DEF1234ghIkl      |
| MONGO_URI      | MongoDB connection string                    | mongodb+srv://user:pass@...  |
| OWNER_ID       | Telegram user ID of bot owner                | 987654321                    |
| BOT_USERNAME   | Bot username (without @)                     | AU_FILESTORE_BOT             |
| CHANNEL_ID     | Channel ID where bot is connected (Database) | -1001234567890               |
| LOG_CHANNEL  | Log channel id | -10987654321 |
## 🤖 Bot Commands

```
start - Start the bot and send direct file to get link (Owner/Admin)
batch - Store multiple messages from channel (Owner/Admin only)
system - Show bot system status (CPU, RAM, uptime, etc.)
id - Get your Telegram user ID
alive - Check bot is alive or not
disclaimer - To Read the copyrights
speedtest - Test server speed
lyrics - search the song name lyrics 
translate - it translate the word is multi language 
stats - Check bot users and statistics (Owner only)
index - check Force sub index added (Owner only)
addfsub - Add a channel to Force Subscribe (Owner | Admin only)
removefsub - Remove a Force Subscribe channel (Owner | Admin only)
fsublist - Show all Force Subscribe channels (Owner | Admin only)
addadmin - Add admin using user id (Owner only)
removeadmin - Remove admin using user id (Owner only)
adminlist - check admins list (Owner only)
ban - ban a user (Owner only)
unban - unban a user (Owner Only) 
banlist - check ban user list (Owner Only)
adddb - to add MongoDB urls (support 5)(Owner only)
removedb - Remove MongoDB url (Owner only)
dblist - check Db lits added (Owner only)
dbstatus - check db is added and online (Owner only)
broadcast - Send message to all users (Owner only)
```
---

### ⚠️ Note
- Only **Owner and Admins** can send files to generate links.
- Batch system works only with **authorized users**.


**NOTE**

```
    Don't Add Values In Config.py , add all Values in Render Only

```

<details><summary>How To Keep Your Bot Alive</summary>
<br>
<b>Use these settings while deploying on Render:</b>
<br><br>
• Runtime: <code>Docker</code>
<br><br>
• Build Command:
<code>pip install -r requirements.txt</code>
<br><br>
• Start Command:
<code>python main.py</code>
<br><br>
<b>🌐 Keep Bot Alive 24/7 Using UptimeRobot</b>
<br><br>
Go to:
https://uptimerobot.com/
<br><br>
Click:
<b>Add New Monitor</b>
<br><br>
Use these settings 👇
<br><br>
<img src="https://telegra.ph/file/a79a156e44f43c9833b50.jpg">
<br><br>
<b>Type:</b>
<code>HTTP(s)</code>
<br><br>
<b>URL:</b>
<code>https://your-render-app.onrender.com</code>
<br><br>
<b>Monitoring Interval:</b>
<code>5 Minutes</code>
<br><br>
After adding monitor click:
<b>Create Monitor</b>
<br><br>
✅ Your bot will stay alive 24/7.
</details>

<details>
<summary><h3>
- <b> ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs </b>
</h3></summary>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʀᴇɴᴅᴇʀ 」─
</h3>
<p align="center"><a href="https://render.com/deploy?repo=https://github.com/Coder-yt/filelinkbot">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a></p>
</details>


  ***Contact Owner***
  
   If you got any error while deploying Contact to Owner 
     
- Developer: <a href="https://t.me/Mr_Mohammed_29"><b>ᴍᴏʜᴀᴍᴍᴇᴅ</b></a>  
- Updates: <a href="https://t.me/Aero_Unity"><b>ᴀᴇʀᴏ ᴜɴɪᴛʏ</b></a>  

---

---

## Fork and ⭐ this repo 
<p align="center">
  If you like this bot, give it a ⭐ on GitHub to support the project!  
  <a href="https://github.com/Coder-yt/filelinkbot" target="_blank">
  </a>
</p>

 ›› **ʏᴏᴜ ᴀʀᴇ ꜰʀᴇᴇ ᴛᴏ ᴜsᴇ, ᴍᴏᴅɪꜰʏ, ᴀɴᴅ sʜᴀʀᴇ ɪᴛ — ʙᴜᴛ ʏᴏᴜ ᴍᴜsᴛ ᴀʟsᴏ ɢɪᴠᴇ ᴄʀᴇᴅɪᴛ**
