import logging

# Get logging configurations
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - Line: %(lineno)d - Path: %(name)s - Module: %(module)s.py - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger().setLevel(logging.WARNING)

import platform
from .config import Config
from pyrogram import Client, __version__, idle
from pyromod import listen


def main():

    Renamer = Client("Compass_Botz",
                 bot_token=Config.BOT_TOKEN,
                 api_id=Config.API_ID,
                 api_hash=Config.API_HASH,
                 plugins=dict(root="renamer/plugins"),
                 workers=100)

    Renamer.start()
    me = Renamer.get_me()

    startup_msg = f"⚡ Boot Successfull at @{me.username}\n"
    startup_msg += f"Pyrogram Version: v{__version__}\n"
    startup_msg += f"Python Version: v{platform.python_version()}\n\n"
    startup_msg += "Deploying has been done. Follow Our Channel @Cinemacollections"
    print(startup_msg)

    idle()

    Renamer.stop()
    print("⛔ Bot Stopped ⛔")

if __name__ == "__main__":
    main()



