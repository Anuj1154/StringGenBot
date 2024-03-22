from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="𝐒𝐓𝐑𝐈𝐍𝐆 𝐒𝐄𝐒𝐒𝐈𝐎𝐍", callback_data="gensession")],
        [
            InlineKeyboardButton(text="𝐌𝐎𝐍𝐒𝐓𝐄𝐑", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="𝐂𝐑𝐄𝐀𝐓𝐎𝐑", url="https://t.me/monster_king_is_here"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝐏𝐑𝐎𝐆𝐑𝐀𝐌 𝐕𝟏", callback_data="pyrogram1"),
            InlineKeyboardButton(text="𝐏𝐑𝐎𝐆𝐑𝐀𝐌 𝐕𝟐", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍", callback_data="gensession")]]
)
