import random
import string
import uuid
import os
os.system('clear')
from faker import Faker
from pystyle import Colors, Colorate
fake = Faker()

def generate_banner():
    banner = '\n                                             ▄█    █▄    \n                                            ███    ███   \n                                            ███    ███   \n                                           ▄███▄▄▄▄███▄▄ \n                                          ▀▀███▀▀▀▀███▀  \n                                            ███    ███   \n                                            ███    ███   \n                                            ███    █▀    \n                                                             \n                             Owner: @Felix_335 | Channel: @FELIXSOFTOOL\n\n    ╭────────────────────────────╮ ╭─────────────────────────────╮ ╭─────────────────────────────╮\n    │  1 • ГЕНЕРАЦИЯ MAC-АДРЕСОВ │ │ 10 • ГЕНЕРАЦИЯ КЛЮЧЕЙ       │ │ 19 • ГЕНЕРАЦИЯ СТАТЕЙ       │ \n    │  2 • ГЕНЕРАЦИЯ IP-АДРЕСОВ  │ │ 11 • ГЕНЕРАЦИЯ ТЕКСТА       │ │ 20 • ГЕНЕРАЦИЯ ИГРОВЫХ НИКОВ│       \n    │  3 • ГЕНЕРАЦИЯ Ф.И.О       │ │ 12 • ГЕНЕРАЦИЯ НОМЕРОВ КАРТ │ │ 21 • ГЕНЕРАЦИЯ СЛУЧАЙНЫХ СОБ│      \n    │  4 • ГЕНЕРАЦИЯ EMAIL       │ │ 13 • ГЕНЕРАЦИЯ ЧИСЕЛ        │ │ 22 • ГЕНЕРАЦИЯ QR-КОДОВ     │\n    │  5 • ГЕНЕРАЦИЯ ЛИЦЕНЗИЙ    │ │ 14 • ГЕНЕРАЦИЯ URL          │ │ 23 • ГЕНЕРАЦИЯ КНИГ         │\n    │  6 • ГЕНЕРАЦИЯ ТЕЛЕФОНОВ   │ │ 15 • ГЕНЕРАЦИЯ ПОЛЬЗОВАТЕЛЕЙ│ │ 24 • ГЕНЕРАЦИЯ ПРИЛОЖЕНИЙ   │\n    │  7 • ГЕНЕРАЦИЯ СЛУЧАЙНЫХ ИМ│ │ 16 • ГЕНЕРАЦИЯ ПРОДУКТОВЫХ  │ │ 25 • ГЕНЕРАЦИЯ ГРУПП        │\n    │  8 • ГЕНЕРАЦИЯ ПАРОЛЕЙ     │ │ 17 • ГЕНЕРАЦИЯ ЗАДАЧ ID     │ │ 26 • ГЕНЕРАЦИЯ АДРЕСОВ      │\n    │  9 • ГЕНЕРАЦИЯ ЛОГИНОВ     │ │ 18 • ГЕНЕРАЦИЯ КОДОВ        │ │ 27 • ГЕНЕРАЦИЯ БИОМЕТРИИ    │\n    ╰────────────────────────────╯ ╰─────────────────────────────╯ ╰─────────────────────────────╯\n         ╭────────────────────────────╮                        ╭────────────────────────────╮\n         │ 28 • ГЕНЕРАЦИЯ ЗАПРОСОВ    │                        │ 29 • ПЕРЕЗАПУСК ГЕНЕРАТОРОВ│\n         ╰────────────────────────────╯                        ╰────────────────────────────╯\n           \n    '
    return Colorate.Horizontal(Colors.purple_to_blue, banner)

def generate_mac_address():
    return ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])

def generate_ip_address():
    return fake.ipv4()

def generate_fio():
    return f'{fake.first_name()} {fake.last_name()}'

def generate_email():
    return fake.email()

def generate_license_key():
    return str(uuid.uuid4()).upper()

def generate_phone_number():
    return fake.phone_number()

def generate_random_name():
    return fake.name()

def generate_password(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_login():
    return fake.user_name()

def generate_keys():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))

def generate_text():
    return fake.text()

def generate_credit_card():
    return fake.credit_card_number(card_type='visa')

def generate_random_number():
    return random.randint(1, 100)

def generate_url():
    return fake.url()

def generate_user():
    return fake.simple_profile()

def generate_product_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def generate_task_id():
    return str(uuid.uuid4())

def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_article():
    return fake.sentence()

def generate_gaming_nick():
    return fake.user_name()

def generate_random_event():
    return fake.bs()

def generate_qr_code():
    return fake.ean13()

def generate_book():
    return fake.sentence(nb_words=4)

def generate_app():
    return fake.company()

def generate_group():
    return fake.company_suffix()

def generate_address():
    return fake.address()

def generate_biometrics():
    return f'Рост: {random.randint(150, 200)} см, Вес: {random.randint(50, 120)} кг'

def generate_request():
    return fake.bs()

def main():
    while True:
        print(generate_banner())
        choice = input('Выбери опцию (1-29): ')
        generators = {'1': generate_mac_address, '2': generate_ip_address, '3': generate_fio, '4': generate_email, '5': generate_license_key, '6': generate_phone_number, '7': generate_random_name, '8': generate_password, '9': generate_login, '10': generate_keys, '11': generate_text, '12': generate_credit_card, '13': generate_random_number, '14': generate_url, '15': generate_user, '16': generate_product_code, '17': generate_task_id, '18': generate_code, '19': generate_article, '20': generate_gaming_nick, '21': generate_random_event, '22': generate_qr_code, '23': generate_book, '24': generate_app, '25': generate_group, '26': generate_address, '27': generate_biometrics, '28': generate_request}
        if choice == '29':
            print('Перезапуск генератор меню...\n')
            continue
        elif choice in generators:
            print(generators[choice]())
        else:
            print('Неверный выбор. Попробуйте еще раз.')
if __name__ == '__main__':
    main()
