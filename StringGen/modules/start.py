from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"𝐻𝐸𝑌 {message.from_user.first_name},\n\n☠️ 𝑇𝐻𝐼𝑆 𝐼𝑆 {Anony.mention},\n𝐴𝑁 𝑂𝑃𝐸𝑁 𝑆𝑂𝑈𝑅𝐶𝐸 𝑆𝑇𝑅𝐼𝑁𝐺 𝐺𝐸𝑁𝐸𝑅𝐴𝑇𝑂𝑅 𝐵𝑂𝑇 , 𝑊𝑅𝐼𝑇𝐼𝑁𝐺 𝐼𝑁 𝑃𝑌𝑇𝐻𝑂𝑁 𝑊𝐼𝑇𝐻 𝑇𝐻𝐸 𝐻𝐸𝐿𝑃 𝑂𝐹 𝑃𝑅𝑂𝐺𝑅𝐴𝑀.,\n\n☠️𝗘𝗡𝗝𝗢𝗬 𝗠𝗢𝗡𝗦𝗧𝗘𝗥 𝗦𝗢𝗖𝗜𝗘𝗧𝗬 ☠️.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
