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
        btn = InlineKeyboardMarkup([[InlineKeyboardButton("🎥 JOIN UPDATE CHANNEL 🎥", url="https://t.me/REQUSET_ACCEPT_BOT")]])
        await message.reply_text(text=f"__Hey 👋{message.from_user.mention},\n\nIm auto delete bot for this group.\n\nUp Time : {up_time}__",
            reply_markup=btn)

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close":
        await query.message.delete()
    elif query.data == "free":
        await query.answer(
            "Please Make me admin in your group for free plan",
            show_alert=True)
    elif query.data == "premium":
        btn = [[
            InlineKeyboardButton("Contact", url="https://t.me/UnKn0wN_DeViL"),
            InlineKeyboardButton("Back", callback_data="back")
        ]]
        reply_markup = InlineKeyboardMarkup(btn)
        await query.message.edit_text(
            text="Please Contact my oowner",
            reply_markup=reply_markup)
    elif query.data == "back":
        btn = [[
            InlineKeyboardButton("Free Plan", callback_data="free"),
            InlineKeyboardButton("Premium Plan", callback_data="premium")
        ],[
            InlineKeyboardButton("Close", callback_data="close")
        ]]
        reply_markup = InlineKeyboardMarkup(btn)
        await query.message.edit_text(text="""**FREE PLAN**
__Delete messages from users.
Will not delete mesaages from another bots 
Maximum deletion time - 30 minutes__

**PREMIUM PLAN**
__Delete all messages ( even messages from other bots ).
Set delete interval upto 10 days.
Plan Cost - Rs.39 / month.__""",
        reply_markup=reply_markup)
        
