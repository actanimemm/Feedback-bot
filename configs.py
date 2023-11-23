import os

class Config(object):

    API_ID = 28090485 #int(os.environ.get("API_ID", 12345))

    API_HASH = "d2cbcc3d47fdb27530eb4f29fbe80534" #str(os.environ.get("API_HASH", ""))

    BOT_TOKEN = "6331931197:AAE_FLEMOxD8fMM5y5bxLAKixqmxZWy3ZYc" #str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = 1056176500 #int(os.environ.get("OWNER_ID", 1428968542))

    AUTH_USERS = set(int(x) for x in "1056176500 1056176500".split())#set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    START = "Start text"#str(os.environ.get("START_TEXT", ""))

    HELP = "Help text" #str(os.environ.get("HELP_TEXT", ""))

    DONATE = "Donate text"#str(os.environ.get("DONATE_TEXT", ""))

    DONATE_LINK = "https://t.me/actanibot"#str(os.environ.get("DONATE_LINK", ""))

    UPDATE_CHANNEL = "https://t.me/actanimemm" #str(os.environ.get("UPDATE_CHANNEL", ""))

    SUPPORT_GROUP = "https://t.me/actanimemmo" #str(os.environ.get("SUPPORT_GROUP", ""))

    DB_URL = "mongodb+srv://actnat:actnat@cluster0.hmlrpgv.mongodb.net/?retryWrites=true&w=majority" #str(os.environ.get("DB_URL", ""))
    
    DB_NAME = "actfeedback-bot" #str(os.environ.get("DB_NAME", ""))
    
    LOG_CHANNEL = -1002004340562#int(os.environ.get("LOG_CHANNEL", ""))

    BROADCAST_AS_COPY = False #bool(os.environ.get("BROADCAST_AS_COPY", True))

