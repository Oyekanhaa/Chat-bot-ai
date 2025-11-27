from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "25742938"
# -------------------------------------------------------------
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7682307978"))
BOT_ID = int(getenv("BOT_ID", "8325048549"))
SUPPORT_GRP = "kanhasworld"
UPDATE_CHNL = "aboutkanha"
OWNER_USERNAME = "Oyekanhaa"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1003370616566"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7682307978").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/korean009/Chat-bot-ai",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
