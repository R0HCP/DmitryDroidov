#недостижимый код, забей хуй на него
def create():
    # Получение данных от пользователя
    api_id = input("Введите ваше имя: ")
    api_hash = input("Введите ваш возраст: ")
    google_api_key = input("Введите ваш город: ")

    # Запись данных в файл
    with open('user_data.txt', 'w') as file:
        file.write(f'api_id = "{api_id}"\n')
        file.write(f'api_hash = "{api_hash}"\n')
        file.write(f'google_api_key = "{google_api_key}"\n')

    print("Данные успешно записаны в файл 'user_data.txt'.")
