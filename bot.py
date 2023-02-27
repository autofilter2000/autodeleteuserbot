import logging
import logging.config
from pyrogram import Client, __version__, types
from pyrogram.raw.all import layer
from config import Config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

User = Client(
    "Delete User Bot", 
    Config.API_ID, 
    Config.API_HASH, 
    workers=200000,
    session_string=Config.USER_SESSION,
    plugins={"root": "user_plugins"})

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="Delete Bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=300000,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
        
    async def start(self):
        await super().start()
        await User.start()
        self._____ = User
        me = await self.get_me()
        ur = await User.get_me()
        self.username = '@' + me.username
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(f"{ur.first_name} User started..thanks to @mayflower68")

    async def stop(self, *args):
        await User.stop()
        await super().stop()
        logging.info("Bot stopped. Bye.")
        
        
        
app = Bot()
app.run()
