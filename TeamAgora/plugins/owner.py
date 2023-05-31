from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from TeamAgora import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/33f3c64764afa143d7243.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩𝗠𝗥 𝗥𝗜𝗗𝗘𝗥𓆪", url=f"https://t.me/xo_tera_baap_on_fire")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/33f3c64764afa143d7243.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩𝗠𝗥 𝗥𝗜𝗗𝗘𝗥𓆪", url=f"https://t.me/xo_tera_baap_on_fire")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("baby")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/33f3c64764afa143d7243.jpg",
        caption=f"""🦋•────────────────•🦋 \n          𝗚𝗬𝗠 🏋‍♂ ✚ 𝗖𝗢𝗖𝗢𝗡𝗨𝗧 𝗪𝗔𝗧𝗘𝗥 🥳 ✚ 𝗢𝗙𝗙𝗜𝗖𝗘 👨‍💻 ✚ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 ✈ ✚ 𝗦𝗟𝗘𝗘𝗣 💤 ✚ 𝗥𝗘𝗣𝗘𝗔𝗧 🔂
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝗕𝗜𝗡𝗔 👩‍🦱 𝗡𝗔 ☝️ 𝗣𝗔𝗟 𝗛𝗢 , 𝗡𝗔 𝗕𝗜𝗡 👆 𝗞𝗔𝗕𝗛𝗜 𝗞𝗔𝗟 𝗛𝗢,
𝗬𝗘 ❤‍🔥  𝗕𝗔𝗡𝗝𝗔𝗬𝗘 🗿 𝗞𝗔 𝗡𝗔 𝗜𝗦𝗠𝗔𝗜 𝗞𝗢𝗜 𝗛𝗔𝗟𝗖𝗛𝗔𝗟 𝗛𝗢

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩𝗠𝗥 𝗥𝗜𝗗𝗘𝗥𓆪", url=f"https://t.me/xo_tera_baap_on_fire")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("baby")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/33f3c64764afa143d7243.jpg",
        caption=f"""🦋•────────────────•🦋 \n          𝗚𝗬𝗠 🏋‍♂ ✚ 𝗖𝗢𝗖𝗢𝗡𝗨𝗧 𝗪𝗔𝗧𝗘𝗥 🥳 ✚ 𝗢𝗙𝗙𝗜𝗖𝗘 👨‍💻 ✚ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 ✈ ✚ 𝗦𝗟𝗘𝗘𝗣 💤 ✚ 𝗥𝗘𝗣𝗘𝗔𝗧 🔂
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝗕𝗜𝗡𝗔 👩‍🦱 𝗡𝗔 ☝️ 𝗣𝗔𝗟 𝗛𝗢 , 𝗡𝗔 𝗕𝗜𝗡 👆 𝗞𝗔𝗕𝗛𝗜 𝗞𝗔𝗟 𝗛𝗢,
𝗬𝗘 ❤‍🔥  𝗕𝗔𝗡𝗝𝗔𝗬𝗘 🗿 𝗞𝗔 𝗡𝗔 𝗜𝗦𝗠𝗔𝗜 𝗞𝗢𝗜 𝗛𝗔𝗟𝗖𝗛𝗔𝗟 𝗛𝗢

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩𓆩𝗠𝗥 𝗥𝗜𝗗𝗘𝗥𓆪", url=f"https://t.me/xo_tera_baap_on_fire")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("agora")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/33f3c64764afa143d7243.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩𝗠𝗥 𝗥𝗜𝗗𝗘𝗥𓆪", url=f"https://t.me/xo_tera_baap_on_fire")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("agora")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/33f3c64764afa143d7243.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩𝗠𝗥 𝗥𝗜𝗗𝗘𝗥𓆪", url=f"https://t.me/xo_tera_baap_on_fire")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("agora")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/33f3c64764afa143d7243.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩𝗠𝗥 𝗥𝗜𝗗𝗘𝗥𓆪", url=f"https://t.me/xo_tera_baap_on_fire")
                ]
            ]
        ),
    )
