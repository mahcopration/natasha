#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6533258434:AAHHCnK3IFq3VM5auSkQJxdVZzOqvLUyGBU")

TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", "MiyaQueenBot")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10917377"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "22bfe49f4482c5cb5424729249a5f097")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002032910706"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6112399514"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mhsm:mhsm@cluster0.j9figvh.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "miyabot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001938180288"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hey dear {first}\n\nIt's Me Miya 🥵.")
try:
    ADMINS=[6112399514]
    for x in (os.environ.get("ADMINS", "6412533552").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hey dear {first}\n\nI'm Miya 🥵 & You Have To Join My 1 Backup Channel After That You Can Get What You Want !\n\n<b>Kindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "JOIN - https://t.me/+O6a66HwHm5phM2U1")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Sorry But I Can't Reply You There 🥲💕"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
