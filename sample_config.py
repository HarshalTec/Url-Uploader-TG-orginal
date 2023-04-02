import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6127937943:AAHOzm_n6fbT0TbUPmJmFj26-QZvJcFHbVE")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 21941890))
    API_HASH = os.environ.get("API_HASH",a192de10945cf3685dbe8ae711b238d8)
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = None #os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/e179e1eb3ab53f14e8788.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "103.51.153.82:32650")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "https://telegra.ph/file/e179e1eb3ab53f14e8788.jpg"
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "1366318700"))
    # database session name(mongoDb)
    SESSION_NAME = os.environ.get("SESSION_NAME", "Cluster0")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Harsh:Harsh9421806556@cluster0.2y4oa4n.mongodb.net/?retryWrites=true&w=majority")
