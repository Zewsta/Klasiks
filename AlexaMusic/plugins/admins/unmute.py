# Copyright (C) 2024 by Klasik_Help @ Github, < https://github.com/TheTeamKlasik >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Klasik © Yukki.

""""
TheTeamKlasik is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Klasik <https://github.com/TheTeamKlasik>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from KlasikMuzik import app
from KlasikMuzik.core.call import Klasik
from KlasikMuzik.utils.database import is_muted, mute_off
from KlasikMuzik.utils.decorators import AdminRightsCheck

# Commands
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")


@app.on_message(filters.command(UNMUTE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_7"], disable_web_page_preview=True)
    await mute_off(chat_id)
    await Klasik.unmute_stream(chat_id)
    await message.reply_text(
        _["admin_8"].format(message.from_user.mention), disable_web_page_preview=True
    )
