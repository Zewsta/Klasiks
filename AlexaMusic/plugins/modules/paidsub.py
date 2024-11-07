# Copyright (C) 2024 by Klasik_Help @ Github, < https://github.com/TheTeamKlasik >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Klasik © Yukki.

""""
TheTeamKlasik is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Klasik <https://github.com/TheTeamKlasik>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
from KlasikMuzik import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from KlasikMuzik.core.mongo import db as Klasik
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from KlasikMuzik.utils.database import get_served_users, get_served_chats


OWNER_ID = 6174058850
