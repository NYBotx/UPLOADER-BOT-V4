# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
import logging

# Regex for ID pattern check (optional, retained from original)
id_pattern = re.compile(r'^.\d+$')


def is_enabled(value, default=False):
    if isinstance(value, str):
        return value.lower() in ["true", "yes", "1", "enable", "y"]
    return default


# Logger setup
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.txt'),
        logging.StreamHandler()
    ],
    level=logging.INFO
)


class Config(object):
    # ========== Basic Bot Info ==========
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Url_Uploader_NY_Bot")
    API_ID = int(os.getenv("API_ID", "24720215"))
    API_HASH = os.getenv("API_HASH", "c0d3395590fecba19985f95d6300785e")

    # ========== Downloads ==========
    DOWNLOAD_LOCATION = os.getenv("DOWNLOAD_LOCATION", "./DOWNLOADS")
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 2194304000))
    TG_MAX_FILE_SIZE = int(os.getenv("TG_MAX_FILE_SIZE", 2194304000))
    FREE_USER_MAX_FILE_SIZE = int(os.getenv("FREE_USER_MAX_FILE_SIZE", 2194304000))
    TG_MIN_FILE_SIZE = int(os.getenv("TG_MIN_FILE_SIZE", 2194304000))
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 128))

    # ========== Thumbnail and Proxy ==========
    DEF_THUMB_NAIL_VID_S = os.getenv("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    HTTP_PROXY = os.getenv("HTTP_PROXY", "")

    # ========== Limits and Timeout ==========
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = int(os.getenv("PROCESS_MAX_TIMEOUT", 3600))

    # ========== MongoDB ==========
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )

    # ========== Session / Identity ==========
    SESSION_NAME = os.getenv("SESSION_NAME", "Url_Uploader_NY_Bot")
    SESSION_STR = os.getenv("SESSION_STR", "")
    OWNER_ID = int(os.getenv("OWNER_ID", "7910994767"))

    # ========== Channels ==========
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002732334186"))
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1002465691872")
    UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "-1002465691872")

    # ========== Shortlink ==========
    SHORT_DOMAIN = os.getenv("SHORT_DOMAIN", "")
    SHORT_API = os.getenv("SHORT_API", "")
    SHORTLINK_ENABLED = is_enabled(os.getenv("SHORTLINK_ENABLED", "false"))
    TUTORIAL_LINK = os.getenv("TUTORIAL_LINK", "https://t.me/How_To_Open_Linkl")

    # ========== Bot Behavior ==========
    TRUE_OR_FALSE = is_enabled(os.getenv("TRUE_OR_FALSE", "false"))
    ADL_BOT_RQ = {}

    # ========== Watermark ==========
    DEF_WATER_MARK_FILE = "@UploaderXNTBot"

    # ========== Banned Users ==========
    BANNED_USERS = set(
        int(x) for x in os.getenv("BANNED_USERS", "").split() if x.strip().isdigit()
    )

    # ========== Other Optional ==========
    MAX_RESULTS = os.getenv("MAX_RESULTS", "50")

    # ========== Logging ==========
    LOGGER = logging
