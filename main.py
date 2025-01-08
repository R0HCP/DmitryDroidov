from telethon import TelegramClient, events, sync
# if u clone this repo u have to create config.py by yourself
import config as config
import texting



client = TelegramClient('test', config.api_id, config.api_hash)  #это создание сесси в телеге
texting.dm(client) 