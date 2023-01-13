import logging
import logging.config
import time

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

BOT_START_TIME = time.time()

def time_formatter(seconds: float) -> str:
    """ humanize time """
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "")
    return tmp[:-2]

    
@Client.on_message(filters.command('start') & filters.private)
async def star_t(bot, message):
    try:
        up_time = time_formatter(time.time() - BOT_START_TIME)
        btn = [[InlineKeyboardButton("OWNER",url="https://t.me/Px1sellerrdp")]]
        reply_markup=InlineKeyboardMarkup(btn)
        await message.reply_text(text=f"__Hey 👋{message.from_user.mention},\n\nIm auto delete bot for this group.\n\nUp Time : {up_time}__",
            reply_markup=reply_markup)
    except Exception as e:
        logging.info(e) 

