from telethon import events, Button, custom
import re, os
from HYPERX.events import register
from HYPERX import telethn as tbot
from HYPERX import telethn as tgbot
PHOTO = "https://telegra.ph/file/71406119a6df4203ffb44.jpg"
@register(pattern=("/alive"))
async def awake(event):
  HYPERx = event.sender.first_name
  HYPERX = "ð¥ððððð ðððð ðð ð·ðð¿ð´ð ðð¥ \n\n"
  HYPERX += "ððð ðððððð ððððððð ðððððððð\n\n"
  HYPERX += "ðððð ððððððð\n\n"
  HYPERX += "ðððððððð : ð­.ð®ð¯.ð¬ ðððððð\n\n"
  HYPERX += "ðððððð ððð ðððððð ðð ðððð"
  BUTTON = [[Button.url("ð¦ð¨ð£ð£ð¢ð¥ð§", "https://t.me/HYPER_X_SUPPORT"), Button.url("ððððððð", "https://t.me/HYPERx_UPDATES")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=HYPERX,  buttons=BUTTON)


__mod_name__ = "Aliveâï¸"
