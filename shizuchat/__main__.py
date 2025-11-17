# main.py
import uvloop
uvloop.install()

import sys
import asyncio
import importlib
import threading

from pyrogram import idle
from pyrogram.types import BotCommand

from . import shizuchat
from database import mongodb
from scheduler import scheduler
from server import run_flask
from config import OWNER_ID
from shizuchat.modules import ALL_MODULES
from logger import LOGGER


async def boot():
    try:
        await shizuchat.start()
    except Exception as ex:
        LOGGER.error(f"Start Error: {ex}")
        sys.exit(1)

    # import modules
    for module in ALL_MODULES:
        importlib.import_module("shizuchat.modules." + module)
        LOGGER.info(f"Imported module: {module}")

    # set bot commands
    try:
        await shizuchat.set_bot_commands(
            [
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Help menu"),
                BotCommand("ping", "Check bot status"),
                BotCommand("shipping", "Couples of the Day"),
                BotCommand("rankings", "User msg leaderboard"),
            ]
        )
        LOGGER.info("Bot commands set.")
    except Exception as ex:
        LOGGER.error(f"Bot command error: {ex}")

    # Notify owner
    try:
        await shizuchat.send_message(OWNER_ID, f"{shizuchat.mention} is now online.")
    except:
        LOGGER.info("Bot started, but owner didn't receive the message.")

    await idle()


if __name__ == "__main__":
    # start flask in separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # run bot
    asyncio.get_event_loop().run_until_complete(boot())
    LOGGER.info("Stopping shizuchat...")
