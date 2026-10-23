#Инструменты

def save_note(text):
    with open('notes.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')

    return 'Заметка сохранена'


def read_notes():
    try:
        with open('notes.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return 'Заметки пока нет'

def hello():
    return 'Привет! Я твой ИИ-агент'

def count_notes():
    try:
        with open('notes.txt', 'r', encoding='utf-8') as file:
            return f"Всего заметок: {len(file.readlines())}"
    except FileNotFoundError:
        return "Всего заметок: 0"

def clear_notes():
    with open('notes.txt', 'w', encoding='utf-8') as file: 
        return 'Удаление прошло успешно'

def search_notes(text):
    try:
        with open('notes.txt', 'r', encoding='utf-8') as file:
            results = []

            for line in file:
                if text.lower() in line.lower():
                    results.append(line.strip())

            if results:
                return f"Всего нашлось: {len(results)}\n" + '\n'.join(results)

            return 'Заметки не найдены.'

    except FileNotFoundError:
        return 'Заметок пока нет.'


#Список инструментов

tools = {
    'привет' : hello,
    'покажи заметки' : read_notes,
    'сколько заметок' : count_notes,
    'запомни' : save_note,
    'очисти заметки' : clear_notes,
    'найди' : search_notes
}


#Часть сообщений

def agent(message):
    for command, function in sorted(
        tools.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        if message == command:
            if command in ('запомни', 'найди'):
                return 'Напиши текст.'
            return function()
        if message.startswith(command + ' '):
            argument = message[len(command) + 1:]
            if command in ('запомни', 'найди'):
                return function(argument)

    return 'Неизвестная команда'
    

#Цыкл

while True:
    message = input('Ты: ').strip().lower()

    if message == 'выход':
        print('Агент завершил работу.')
        break

    response = agent(message)
    print('Агент:', response)