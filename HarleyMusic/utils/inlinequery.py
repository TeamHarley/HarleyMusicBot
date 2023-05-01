#
# Copyright (C) 2021-2022 by TeamHarley@Github, < https://github.com/TeamHarley >.
#
# This file is part of < https://github.com/TeamHarley/Harley MusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamHarley/HarleyMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause Stream",
            description=f"Pause the current playout on group call.",
            thumb_url="https://telegra.ph/file/95f3f7557f5dfc919dda6.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume Stream",
            description=f"Resume the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/ab79a890fc3f33b6f282d.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Mute Stream",
            description=f"Mute the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/89743818010d21d36f66f.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Unmute Stream",
            description=f"Unmute the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Skip Stream",
            description=f"Skip to next track. | For Specific track number: /skip [number] ",
            thumb_url="https://telegra.ph/file/ffd842fe57ebc86c906e2.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End Stream",
            description="Stop the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/bdb7359fbb11052ced09c.jpg",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Stream",
            description="Shuffle the queued tracks list.",
            thumb_url="https://telegra.ph/file/cb0ab21555f9fb12c49e7.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Seek Stream",
            description="Seek the ongoing stream to a specific duration.",
            thumb_url="https://telegra.ph/file/af5e903bb23e0b77540c0.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Loop Stream",
            description="Loop the current playing music. | Usage: /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/674c509779cf866a6e8d8.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
