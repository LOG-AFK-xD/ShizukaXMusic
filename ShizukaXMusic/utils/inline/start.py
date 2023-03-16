from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from ShizukaXMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me Your Group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Help",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Settings", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me Your Group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Help", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Group", url=f"{SUPPORT_GROUP}"
            ),
            InlineKeyboardButton(
                text="Creator", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="Language",
                callback_data="LG",
            )
        ],
     ]
    return buttons
