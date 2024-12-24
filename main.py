from telethon import TelegramClient, events, sync
 # if u clone this repo u have to create config.py by yourself
from config import api_id, api_hash, konstantin, igor, google_api_key, me
from bard import answer
import io 
import sys 
import datetime

client = TelegramClient('test', api_id, api_hash)
victim = igor
 
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

async def main():
    await client.start()
    print(datetime.datetime.now())
    await client.send_message(victim, answer("ты начинаешь диалог с человеком, дай ему инструкцию что если он хочет завершить диалог то он должен написать завершить с маленькой буквы"))
    
    print("отправил")
    await client.run_until_disconnected()

with client: #here all shit begins
    client.loop.run_until_complete(main())


