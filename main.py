from telethon import TelegramClient, events, sync
 # if u clone this repo u have to create config.py by yourself
from config import api_id, api_hash, konstantin, igor, google_api_key, me
from bard import answer
import io 
import sys 
import datetime
import random

client = TelegramClient('test', api_id, api_hash)
 
@client.on(events.NewMessage(from_users=victim))
async def my_event_handler(event):
    print("принял", event.raw_text)

    try:
        if event.raw_text == 'завершить': 
            await client.send_message(victim, answer(event.raw_text + "обязательно не забудь послать меня нахуй") + "\n пока")
            await client.disconnect()
        else:
            await client.send_message(victim, answer(event.raw_text))
    except Exception as e:
        print(f"Произошла ошибка: {e}")








# excluded_user = "Dmitry_Droidov"

# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     print("принял", event.raw_text)

#     chance = random.randint(1, 100000)
#     print (chance)
#     if chance <= 1488 or event.raw_text == 'завершить':
#         if event.sender.username != excluded_user:
#             try:
#                 if event.raw_text == 'завершить': 
#                     await client.send_message(victim, answer("это твое посленднее сообщеник обязательно не забудь послать меня нахуй") + "\n пока")
#                     if random.randint(1, 100000) < 1337:
#                         await client.disconnect()
#                 else:
#                     await client.send_message(victim, answer(event.raw_text))   
#             except Exception as e:
#                 print(f"Произошла ошибка: {e}")

async def main():
    await client.start()
    print(datetime.datetime.now())
    await client.send_message(victim, answer("Пошути"))
    
    print("отправил")
    await client.run_until_disconnected()

with client: #here all shit begins
    client.loop.run_until_complete(main())


