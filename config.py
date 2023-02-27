import os
from dotenv import load_dotenv

load_dotenv(".env")


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    USER_SESSION = os.environ.get("USER_SESSION", "")
    TIME_GAP = int(os.environ.get("TIME_GAP", "")) # in seconds
   # AUTH_CHATS = [int(user) for user in (os.environ.get("AUTH_CHATS", "")).split()]
    OWNER = [int(user) for user in (os.environ.get("OWNER", "")).split()]
    
