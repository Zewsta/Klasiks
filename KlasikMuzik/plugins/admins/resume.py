from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from KlasikMuzik import app
from KlasikMuzik.core.call import Klasik
from KlasikMuzik.utils.database import is_Muzik_playing, Muzik_on
from KlasikMuzik.utils.decorators import AdminRightsCheck

# Komut
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(filters.command(RESUME_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_Muzik_playing(chat_id):
        return await message.reply_text(_["admin_3"], disable_web_page_preview=True)
    await Muzik_on(chat_id)
    await Klasik.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), disable_web_page_preview=True
    )
