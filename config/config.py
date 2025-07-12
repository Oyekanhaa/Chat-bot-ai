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
OWNER_ID = int(getenv("OWNER_ID", "7009601543"))
BOT_ID = int(getenv("BOT_ID", "8113054986"))
SUPPORT_GRP = "PBX_CHAT"
UPDATE_CHNL = "HEROKUBIN_01"
OWNER_USERNAME = "ll_BAD_MUNDA_ll"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002056907061"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7009601543").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://gitlab.com/Badhacker98/Chatbot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
