# Copyright (C) 2024 by Klasik_Help @ Github, < https://github.com/TheTeamKlasik >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Klasik © Yukki.

""""
TheTeamKlasik is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Klasik <https://github.com/TheTeamKlasik>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from config import LOG, LOG_GROUP_ID, Muzik_BOT_NAME
from KlasikMuzik.utils.database import is_on_off
from KlasikMuzik import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**💞 {Muzik_BOT_NAME} ᴍᴜsɪᴄ ʟᴏɢs **
**━━━━━━━━━━━━━━━**
**🌹️ 𝐂𝐡𝐚𝐭 𝐍𝐚𝐌𝐞 : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**🥀 𝐍𝐚𝐌𝐞 : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**🌸 𝐔𝐬𝐞𝐑𝐧𝐚𝐌𝐞 : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**🌷 𝐈𝐃  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🌿 𝐂𝐡𝐚𝐭 𝐥𝐢𝐧𝐤: >** {chatusername}
**━━━━━━━━━━━━━━━**
**🌻 𝐒𝐞𝐀𝐫𝐜𝐇𝐞𝐝 𝐅𝐨𝐫:** {message.text}
**━━━━━━━━━━━━━━━**
**💐 𝐒𝐭𝐫𝐄𝐚𝐦 𝐓𝐲𝐏𝐞:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
