from pyrogram.emoji import *

class TEXT:
    DOWNLOAD_START = f"**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**"
    UPLOAD_START = f"**📤 ᴜᴘʟᴏᴀᴅɪɴɢ...**"
    UPLOAD_SUCESS = f"ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴜꜱɪɴɢ ᴍᴇ | ꜱʜᴀʀᴇ > ⚡"
    BANNED_USER_TEXT = f"Hey, you are **banned** from using me {FACE_WITH_TEARS_OF_JOY}."
    NOT_LOGGED_TEXT = f"This bot was only for private use {LOCKED_WITH_KEY}. If you want to use this bot you need to send me correct password in the format `/login bot_password`"
    SAVED_CUSTOM_THUMBNAIL = f"**✅ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ**"
    DELETED_CUSTOM_THUMBNAIL = f"**🗑️ ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ**"
    NO_CUSTOM_THUMB_NAIL_FOUND = f"**🙅‍♂️ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜰᴏᴜɴᴅ"
    THUMBNAIL_CAPTION = f"**📲 ʏᴏᴜʀ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ**"


    ABOUT = """**Bot Info**

** ➜ My Name:** {bot_name}
** ➜ Language:** [Python 3](https://www.python.org/)
** ➜ FrameWork:** [Pyrogram](https://github.com/pyrogram/pyrogram)
** ➜ Developer:** {bot_owner}
** ➜ Channel:** [Compass Botz](https://t.me/Compass_Botz)
** ➜ Source Code:** [Press Me](https://github.com/dakshkohli23/New-TG-Rename-Bot)
"""

    HELP_USER = """**Follow Below Steps:**
   
➜ Use /mode command to change upload mode.
➜ Send a photo to set as permanent thumbnail.
➜ Now send me the Telegram file you want to rename.
➜ Send the new name when bot ask.

For Source Code check About Section!
"""

    START_TEXT = """Hey! {user_mention},
I'm Telegram Renamer Bot with Permanent Thumbnail support!⚡.

<b>Do /help for more Details ...</b>
**Maintained By:** {bot_owner}
"""


    DONATE_USER = """**__Thanks for showing interest in donation.__**
 
Donate us to keep our services continously alive
You can send any amount 
of 20rs, 30rs, 50rs, 70rs, 100rs, 200rs
 
__--Payment Methods:--__
 
GooglePay / Paytm / PhonPay / paypal / Net Banking
 
**For Donate:** Message me @Dlaize"""
