import os
from dotenv import load_dotenv

load_dotenv(".env")


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5826709597:AAGEc8QvSWydvfnibhbWjfZP5N7Ah-Ytcgo")
    API_ID = int(os.environ.get("API_ID", "22359038"))
    API_HASH = os.environ.get("API_HASH", "b3901895dc193c30c808ba4f1b550ed0")
    USER_SESSION = os.environ.get("USER_SESSION", "BQGNZREAFn97cLlBEJ4JFqrLUUxbfx3kqaj3mgHPxmLkG1vNvwg60cTh3u35DXrlWdQ3U3ORjtl4_EQAHGAmmiaF8LPr-hEOZC3D_hdYAqPeDNbMhBiOyukQeiudazCaO_MX4rOtCDODvNSwaeXygl3qQ0W3CBSfrQNqUVeuUDWezv7Y0vTt4QdozWb_qWO4wal6n0gDjtFGX5BXiUhHUnxlbfx3NKVllYJTKEs-5DKqJp7Tu_cGSKwwJf-AosGzBWvEcys8d5qZ1gpXNyPYFzveY-CncONOlMijpYZPyjyujverpA2sAG896kYfeT35gu9LUN4YtrWdMtIG_zO2-KQu7riEbgAAAAFMNRQYAA")
    TIME_GAP = int(os.environ.get("TIME_GAP", "300")) # in seconds
   # AUTH_CHATS = [int(user) for user in (os.environ.get("AUTH_CHATS", "")).split()]
    OWNER = [int(user) for user in (os.environ.get("OWNER", "5531461861")).split()]
    
