from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from KlasikMuzik import app
from KlasikMuzik.core.call import Klasik
from KlasikMuzik.utils.database import is_Muzik_playing, Muzik_off
from KlasikMuzik.utils.decorators import AdminRightsCheck

# Komut
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(filters.command(PAUSE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_Muzik_playing(chat_id):
        return await message.reply_text(_["admin_1"], disable_web_page_preview=True)
    await Muzik_off(chat_id)
    await Klasik.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), disable_web_page_preview=True
    )
