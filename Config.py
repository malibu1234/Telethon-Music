import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25302801"))
    API_HASH = os.environ.get("API_HASH", "955818e2e0fa518ca8ab87bdd280b5b4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5688442859:AAHcUUw9VhqIr5XIYleFcEYcFgF7QlkI3wE ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCFVX-4cBsqg5srtn9RO0XMUYEYIepPl6t6m1rxMzEtRLy-Mu2K0j1Q7Y7yrbxL3hJIbj77T06OysHoOICZVg3Gj-so-wqu272QQyKxg_Og2-ohMyLhbgjwZiynMyNw8zrRNU5AfSfFeevwpu1tUOHatLgkivLolseE-0eFf6gR32spLCL3tXMX8vEM4_j5S8JvOSscrm_4eOC-KC9EHw8AOy9QdEJw0HC_JCBTslVL5HK_UjU71-pLwuhh2V7GYv0k2-wMR2H91NwZIJxJLKpnWUqGgGkvwjnkSiZo39OouOj8qDExM--SC7W--_0ETwQbsmZzNR35-DK30nJdApHVAAAAAWFUaEQA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "jimm45bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "jimmy music")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/138ef6b5944b8342159dd.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/138ef6b5944b8342159dd.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5927888964"))
    MONGO_DB_URI = mongodb+srv://manu:Rokiputha.90@cluster0.myho7dn.mongodb.net/?retryWrites=true&w=majority
