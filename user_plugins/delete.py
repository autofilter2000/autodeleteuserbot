#delete
import logging
import logging.config
import time

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
import asyncio
from pyrogram import filters, Client, enums
from config import Config

@Client.on_message(filters.group & (filters.bot|filters.text), group = 1)
async def delete_(client, message):
    userid = message.from_user.id if message.from_user else None
    group_id = message.chat.id
    try:
        st = await client.get_chat_member(group_id, userid)
        if st.status in [enums.ChatMemberStatus.OWNER] or message.from_user.id in Config.OWNER:
            print("You are Admin or Owner of this group")
            return
        else:
            await asyncio.sleep(Config.TIME_GAP)
            await client.delete_messages(
                chat_id=message.chat.id, 
                message_ids=message.id
            )
            print("User Deleted Msg")
    except Exception as e:
        logging.info(e)
