# Copyright (C) 2024 by Klasik_Help @ Github, < https://github.com/TheTeamKlasik >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Klasik © Yukki.

""""
TheTeamKlasik is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Klasik <https://github.com/TheTeamKlasik>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean_copy = autoclean.copy()
        for item in autoclean_copy:
            if item == rem:
                autoclean.remove(item)

        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem and "live_" not in rem and "index_" not in rem:
                try:
                    if os.path.exists(rem):
                        os.remove(rem)
                except:
                    pass
    except:
        pass
