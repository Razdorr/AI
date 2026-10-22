#Инструменты

def save_note(text):
    with open('notes.txt', 'a',
    encoding='utf-8') as file:
        file.write(text + '\n')

    return 'Заметка сохранена'


def read_notes():
    try:
        with open('notes.txt', 'r',
        encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return 'Заметки пока нет'

def hello():
    return 'Привет! Я твой ИИ-агент'

def count_notes():
    try:
        with open('notes.txt', 'r',
        encoding='utf-8') as file:
            return f"Всего заметок: {len(file.readlines())}"
    except FileNotFoundError:
        return "Всего заметок: 0"


#Список инструментов

tools = {
    'привет' : hello,
    'покажи заметки' : read_notes,
    'сколько заметок' : count_notes
}


#Часть сообщений

def agent(message):
    if message.startswith('запомни '):
        text = message[8:]
        return save_note(text)
    elif message in tools:
        return tools[message]()

    return 'Неизвестная команда'
    

#Цыкл

while True:
    message = input('Ты: ').strip().lower()

    if message == 'выход':
        print('Агент завершил работу.')
        break

    response = agent(message)
    print('Агент:', response)