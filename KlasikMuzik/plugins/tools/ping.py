from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, Muzik_BOT_NAME, PING_IMG_URL
from strings import get_command
from KlasikMuzik import app
from KlasikMuzik.core.call import Klasik
from KlasikMuzik.utils import bot_sys_stats
from KlasikMuzik.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(filters.command(PING_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_text(
        text=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Klasik.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, Muzik_BOT_NAME, UP, RAM, CPU, DISK, pytgping)
    )
