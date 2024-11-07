# Copyright (C) 2024 by Klasik_Help @ Github, < https://github.com/TheTeamKlasik >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Klasik © Yukki.

""""
TheTeamKlasik is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Klasik <https://github.com/TheTeamKlasik>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall, GroupCallNotFound

import config
from config import BANNED_USERS
from KlasikMusic import LOGGER, app, userbot
from KlasikMusic.core.call import Klasik
from KlasikMusic.misc import sudo
from KlasikMusic.plugins import ALL_MODULES
from KlasikMusic.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("KlasikMusic").error("Add Pyrogram string session and then try...")
        sys.exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("KlasikMusic.plugins" + all_module)
    LOGGER("KlasikMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Klasik.start()
    try:
        await Klasik.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except (NoActiveGroupCall, GroupCallNotFound):
        LOGGER("KlasikMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await Klasik.decorators()
    LOGGER("KlasikMusic").info("Klasik Music Bot Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("KlasikMusic").info("Stopping Klasik Music Bot...")


if __name__ == "__main__":
    app.run(init())
    LOGGER("KlasikMusic").info("Stopping Music Bot")
