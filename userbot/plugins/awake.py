
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname
from userbot.Config import Var

ALIVE_PIC = Var.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/2f2b8d40e3f2fa4acdc8f.mp4"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Var.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**🔱Black Lightning IS Awake🔱 \n\n\n**"
   ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
   ALIVE_MESSAGE += f"`Telethon: TELETHON-15.0.0 \n\n`"
   ALIVE_MESSAGE += f"`Python: PYTHON-3.8.5 \n\n`"
   ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n\n`"
   ALIVE_MESSAGE += f"`Support Channel` : @blacklightningot \n\n"
   ALIVE_MESSAGE += f"`MY BOSS🤗`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
