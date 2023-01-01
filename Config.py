import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25302801"))
    API_HASH = os.environ.get("API_HASH", "955818e2e0fa518ca8ab87bdd280b5b4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5688442859:AAHcUUw9VhqIr5XIYleFcEYcFgF7QlkI3wE ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKkBu2KSuV0dSTZ0jUMgSTYKGlfSR7bNUTIl4DmoLhY9ZFcWytuV094RaJSAEjWdW2nR4tZW3gL02PIQZdvCUnmhS5mLNbDLFWsO_wyTDXJTkpApiloQfv2vHcLZ-h7u35g8hmh89XSw-kaoXHrvvv2fStHBywdm0gRj44SqJxP7n6B31v_KiE6n1l6WZcStiPSl24CNu8nKJS_yniEDcOp8CNsV8DPS-34HNdwnleiZVU7w1_Z6FahiqqVu2wHdjZh1FJR8_gZBdyX52wGngBWr-cMsr2GzV6zrPJVLwxCKNS7BrtNN4MScCZ0rsSOxaYYaiZKWt0xcMieam0T7cOqmT4w=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "jimm45bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "jimmy music")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/138ef6b5944b8342159dd.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/138ef6b5944b8342159dd.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5927888964"))
    
