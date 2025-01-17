import sqlite3
import json

class Message:
    def __init__(self, userId: int = 0, userName: str = '', displayName: str = '', token: int = 0):
        self.userId = userId
        self.userName = userName
        self.displayName = displayName
        self.token = token


    def to_json(self):
        return json.dumps({
            'userId': self.userId,
            'userName': self.userName,
            'displayName': self.displayName,
            'token': self.token
        })

    def get_all_messages(self): 
        conn = sqlite3.connect('messages.db') 
        cursor = conn.cursor() 
        cursor.execute('SELECT * FROM messages') 
        result = cursor.fetchall() 
        conn.close() 
        return result
    
    def write_token(self, new_token_amount: int):
        self.token = new_token_amount

# Функция для получения токенов по userId
    def get_user_token(userId: int) -> int:
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT token FROM messages WHERE userId = ?
        ''', (userId,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return result[0]
        else:
            return 0  # или любое другое значение по умолчанию, если пользователь не найден


    def reset_all_tokens(self): 
        conn = sqlite3.connect('messages.db') 
        cursor = conn.cursor() 
        cursor.execute(''' UPDATE messages SET token = 0 ''') 
        conn.commit() 
        conn.close()
        

    def save_to_db(self):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        
        # Проверка, существует ли пользователь
        cursor.execute('''
            SELECT token FROM messages WHERE userId = ?
        ''', (self.userId,))
        result = cursor.fetchone()
        
        if result:
            # Обновление токенов для существующего пользователя
            current_token = result[0]
            new_token = current_token + self.token
            cursor.execute('''
                UPDATE messages
                SET token = ?
                WHERE userId = ?
            ''', (new_token, self.userId))
        else:
            # Добавление нового пользователя
            cursor.execute('''
                INSERT INTO messages (userId, userName, displayName, token)
                VALUES (?, ?, ?, ?)
            ''', (self.userId, self.userName, self.displayName, self.token))
        
        conn.commit()
        conn.close()

# Создание и инициализация таблицы базы данных
def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            userName TEXT,
            displayName TEXT,
            token INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    


if __name__ == '__main__':
    # Инициализация базы данных
    init_db()