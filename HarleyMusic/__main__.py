#
# Copyright (C) 2021-2022 by TeamHarley@Github, < https://github.com/TeamHarley >.
#
# This file is part of < https://github.com/TeamHarley/Harley MusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamHarley/HarleyMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from HarleyMusic import LOGGER, app, userbot
from HarleyMusic.core.call import Harley
from HarleyMusic.plugins import ALL_MODULES
from HarleyMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("HarleyMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("HarleyMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
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
        importlib.import_module("HarleyMusic.plugins" + all_module)
    LOGGER("Harleymusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Harley.start()
    try:
        await Harley.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("HarleyMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Harley.decorators()
    LOGGER("HarleyMusic").info("Harley Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("HarleyMusic").info("Stopping Harley Music Bot! GoodBye")
