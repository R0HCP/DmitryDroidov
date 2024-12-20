from telethon import TelegramClient, events, sync
 # if u clone this repo u have to create config.py by yourself
from config import api_id, api_hash, konstantin, igor, google_api_key, me
from bard import ansver
import io 
import sys 
import datetime

client = TelegramClient('test', api_id, api_hash)
victim = "SaIDaI7" 
last = "дарова нига, го творить"

client = TelegramClient('test', api_id, api_hash)

@client.on(events.NewMessage(from_users=victim))
async def my_event_handler(event):
    print("принял", event.raw_text)
    last = event.raw_text
    try:
        if event.raw_text == 'завершить': 
            print(datetime.datetime.now())
            buffer = io.StringIO() 
            sys.stdout = buffer
            ans = ansver(last + "обязательно не забудь послать меня нахуй")
            sys.stdout = sys.__stdout__
            ans = buffer.getvalue()
            print ("🦊🦊🦊"+ans)

            
            print('\n\n\n`шутка кончилась`')

            await client.send_message(victim, ans + "пока")
            await client.disconnect()
        else:
            print(datetime.datetime.now())
            buffer = io.StringIO() 
            sys.stdout = buffer
            ans = ansver(last)
            sys.stdout = sys.__stdout__
            ans = buffer.getvalue()
            print ("🦊🦊🦊"+ans)
            
            print('\n\n\n`шутка кончилась`')
            
            await client.send_message(victim, ans)
            print("отправил к")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

async def main():
    await client.start()
    print(datetime.datetime.now())
    await client.send_message(victim, "напиши завершить если с тебя хватит")
    
        # await client.send_message(victim, "напиши "завершить" когда захочешь завершить /n"+ ansver(last))
    print("отправил")
    await client.run_until_disconnected()

with client: #here all shit begins
    client.loop.run_until_complete(main())


