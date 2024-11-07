import asyncio
from KlasikMuzik import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from KlasikMuzik.core.mongo import db as Klasik
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from KlasikMuzik.utils.database import get_served_users, get_served_chats


OWNER_ID = 8061949128
