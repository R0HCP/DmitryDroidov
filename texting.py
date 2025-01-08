from telethon import TelegramClient, events, sync
import time
from bard import answer
import datetime
from colorama import Fore, Style

def dm(client): 
    @client.on(events.NewMessage)# ждем событие
    async def my_event_handler(event):

        print(datetime.datetime.now())
        sender = await event.get_sender()#вывод в консоль
        print("принял", Fore.GREEN + event.raw_text, Style.RESET_ALL + "\n от пользователя ", Fore.GREEN + "@", sender.username," ", sender.first_name," ", sender.last_name , Style.RESET_ALL + ".")
        
        if event.is_private:#если это личка
            q = answer(event.raw_text)
            await client.send_message(sender,q)
            print ("Отправил: \n", Fore.YELLOW + q + Style.RESET_ALL)
        
        elif event.is_group:#если это группа
            
            print ('Это группа')
            if (event.message.mentioned or  # Проверяем, упомянут ли пользователь
        (event.message.is_reply and (await event.message.get_reply_message()).sender_id == 6373123783)):  # чтоб он сам себе не отвечал
                print (Fore.GREEN + "Упомянут", Style.RESET_ALL)
                try:

                    if event.raw_text != "-смс": await client.send_message(event.chat_id, answer(event.raw_text), reply_to=event.message.id) #чтоб он ирису не отвечал
                except Exception as e:
                    # try:
                    #     if event.raw_text != "-смс": await client.send_message(event.chat_id, f"Произошла ошибка: {e}", reply_to=event.message.id)
                        print(f"Произошла ошибка: {e}")
                    # except Exception as e:
                    #     print(f"с телегой: {e}")
    
    async def main():
        await client.start()
        print(datetime.datetime.now())
        print("А я уже работаю!")
        await client.run_until_disconnected()

    with client: #вызов функции в которой запускается клиент
        client.loop.run_until_complete(main())