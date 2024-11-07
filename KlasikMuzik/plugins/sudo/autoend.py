from pyrogram import filters

import config
from strings import get_command
from KlasikMuzik import app
from KlasikMuzik.misc import SUDOERS
from KlasikMuzik.utils.database import autoend_off, autoend_on
from KlasikMuzik.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**Kullanım:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "**Otomatik Akış Sonlandırma Etkinleştirildi.**\n\n**Asistan Birkaç Dakika Sonra Kimse Dinlemediğinde Bir Uyarı Mesajıyla Görüntülü Sohbetten Otomatik Olarak Ayrılacak‌‌.**"
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Akışı Otomatik Sonlandırma Devre Dışı‌‌.")
    else:
        await message.reply_text(usage)
