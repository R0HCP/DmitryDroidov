from telethon import TelegramClient, events, sync
import time
from bard import answer
import datetime
import Message
from colorama import Fore, Style
from Message import Message, init_db

def dm(client): 
    @client.on(events.NewMessage)# ждем событие
    async def my_event_handler(event):

        print(datetime.datetime.now())
        sender = await event.get_sender()#вывод в консоль
        print("принял", Fore.GREEN + event.raw_text, Style.RESET_ALL + "\n от пользователя ", Fore.GREEN + "@", sender.username," ", sender.first_name," ", sender.last_name , Style.RESET_ALL + ".")
        
        

        if event.is_private:#если это личка
            q, e = answer(event.raw_text, shorting = False)
            try:
                await client.send_message(sender,q)
            except Exception as e:
                print(f"Произошла ошибка: {e}")
            print ("Отправил: \n", Fore.YELLOW + q + Style.RESET_ALL, e)
        
        elif event.is_group:#если это группа
            
            mes = Message(userId=event.sender_id, userName=sender.username, displayName=sender.first_name, token=0) 
            print ('Это группа')
            
            if (event.message.mentioned or  # Проверяем, упомянут ли пользователь
        (event.message.is_reply and (await event.message.get_reply_message()).sender_id == 6373123783)):  # чтоб он сам себе не отвечал
                

                print (Fore.GREEN + "Упомянут", Style.RESET_ALL)

                if event.raw_text == "🦊!!" and event.raw_text != "смс": #вывод
                    mes.reset_all_tokens()
                    try:
                        result = ""
                        for item in mes.get_all_messages(): 
                            id, userId, userName, displayName, token = item
                            # result += f"userName: {userName}, displayName: {displayName}, token: {token}\n"
                            result += f"[{displayName}](t.me/{userName}) - {token}\n"
                        await client.send_message(event.chat_id, result , parse_mode='markdown', link_preview=False, reply_to=event.message.id)
                    except Exception as e:
                        print(f"Произошла ошибка вывода ебать :  {e}")


                if event.raw_text == "🦊🦊🦊🦊" and event.raw_text != "смс": #вывод
                    try:
                        result = ""
                        for item in mes.get_all_messages(): 
                            id, userId, userName, displayName, token = item
                            # result += f"userName: {userName}, displayName: {displayName}, token: {token}\n"
                            result += f"[{displayName}](t.me/{userName}) - {token}\n"
                        await client.send_message(event.chat_id, result , parse_mode='markdown', link_preview=False, reply_to=event.message.id)
                    except Exception as e:
                        print(f"Произошла ошибка вывода ебать :  {e}")
                
                else:
                    if Message.get_user_token(event.sender_id) < 12000:
                        ans, tokens = answer("пользователь с именем" + sender.first_name + "говорит" + event.raw_text, True)
                    else:
                        ans = "вы исчерпали лимит токенов"
                        tokens = 0
                    mes.write_token(tokens)
                    mes.save_to_db()

                    try:

                        if event.raw_text != "-смс": #чтоб он ирису не отвечал

                            await client.send_message(event.chat_id, ans, reply_to=event.message.id) 
                    
                    except Exception as e:
                        try:

                            if event.raw_text != "-смс": 
                                await client.send_message(event.chat_id, f"Произошла ошибка: {e}", reply_to=event.message.id)
                                await client.send_file(event.chat_id, 'sticker.webp')
                            print(f"Произошла ошибка: {e}")
                        except Exception as e:
                            print(f"с телегой: {e}")

    async def main():
        await client.start()
        print(datetime.datetime.now())
        init_db()
        print("А я уже работаю!")
        await client.run_until_disconnected()


    with client: #вызов функции в которой запускается клиент
        client.loop.run_until_complete(main())