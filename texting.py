from telethon import TelegramClient, events, sync
import time
from bard import answer
import datetime
from colorama import Fore, Style, init

def dm(client): 
    @client.on(events.NewMessage)
    async def my_event_handler(event):
        print(datetime.datetime.now())
        print("принял", Fore.GREEN + event.raw_text, Fore.BLACK + "\n от пользователя ", Fore.GREEN + str(event.get_sender()), Fore.BLACK + ".")
        sender = await event.get_sender()
        
        if event.is_private:
            q = answer(event.raw_text)
            if event.raw_text != "-смс": await client.send_message(sender,q)
            print ("Отправил: \n", Fore.YELLOW + q + Style.RESET_ALL)
        elif event.is_group:
            if (event.message.mentioned or  # Проверяем, упомянут ли пользователь
        (event.message.is_reply and (await event.message.get_reply_message()).sender_id == 6373123783)):  # Проверяем, является ли сообщение ответом от target_user
                print ('Это группа')
                try:
                    if event.raw_text != "-смс": await client.send_message(event.chat_id, answer(event.raw_text), reply_to=event.message.id)
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
    
    async def main():
        await client.start()
        print(datetime.datetime.now())
        print("отправил")
        await client.run_until_disconnected()

    with client: #here all shit begins
        client.loop.run_until_complete(main())


    