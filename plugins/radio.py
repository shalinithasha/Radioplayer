"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from utils.vc import mp, RADIO
from config import Config
STREAM_URL=Config.STREAM_URL
ADMINS=Config.ADMINS

@Client.on_message(filters.command("radio") & filters.user(ADMINS))
async def radio(client, message: Message):
    if 1 in RADIO:
        await message.reply_text(f"{emoji.ROBOT} **කරුණාකර /stopradio විධානය මඟින් පවතින ගුවන්විදුලි ප්‍රවාහය නවත්වන්න!**")
        return
    await mp.start_radio()
    await message.reply_text(f"{emoji.CHECK_MARK_BUTTON} **ගුවන්විදුලි ප්‍රවාහය ආරම්භ විය :** \n<code>{STREAM_URL}</code>")

@Client.on_message(filters.command("stopradio") & filters.user(ADMINS))
async def stop(_, message: Message):
    if 0 in RADIO:
        await message.reply_text(f"{emoji.ROBOT} **කරුණාකර / radio විධානය මඟින් පළමුව රේඩියෝ ප්‍රවාහයක් ආරම්භ කරන්න!**")
        return
    await mp.stop_radio()
    await message.reply_text(f"{emoji.CROSS_MARK_BUTTON} **ගුවන්විදුලි ප්‍රවාහය සාර්ථකව අවසන් විය!**")
