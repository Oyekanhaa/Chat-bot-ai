import os
import random
import time
from shizuchat import shizuchat
from config import OWNER_USERNAME
import requests
from pyrogram.types import  Message
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from BadAPI import api
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters


@shizuchat.on_cmd(["ai", "chatgpt"])
async def chat_gpt(bot, message):
    
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "ᴇx. /ai ᴡʜᴇʀᴇ ɪs ɢᴏʟᴅᴇɴ ᴛᴇᴍᴘʟᴇ ?")
        else:
            a = message.text.split(' ', 1)[1]
            r=api.gemini(a)["results"]
            await message.reply_text(f" {r} \n\n🌸  ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ [ʙᴀᴅ ᴍᴜɴᴅᴀ](https://t.me/{OWNER_USERNAME}) ||", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
