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


def agent(message):
    if message.startswith('запомни '):
        text = message[8:]
        return save_note(text)
    
    elif message == 'привет':
        return 'Привет! Я твой ИИ-агент.'

    elif message == 'покажи заметки':
        return read_notes()

    else:
        return 'Пока я не умею выполнять эту команду'



while True:
    message = input('Ты: ').strip().lower()

    if message == 'выход':
        print('Агент завершил работу.')
        break

    response = agent(message)
    print('Агент:', response)