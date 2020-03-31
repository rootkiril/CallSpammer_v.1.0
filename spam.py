from service import *
import os
import re
from colorama import Fore, init, Style


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def is_allowed_str(string):
    char_regex = re.compile(r'[^а-яА-ЯєіїЄІЇ]')
    string = char_regex.search(string)
    return not bool(string)


def is_allowed_num(string):
    char_regex = re.compile(r'[^0-9]')
    string = char_regex.search(string)
    return not bool(string)


def main():
    init(autoreset=True)
    print(Fore.YELLOW + """
      _____      _ _  _____                                           
     / ____|    | | |/ ____|      UKRAINE                                     
    | |     __ _| | | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
    | |    / _` | | |\___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
    | |___| (_| | | |____) | |_) | (_| | | | | | | | | | | |  __/ |   
     \_____\__,_|_|_|_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                           | |                                     
                  v.1.0    |_|  telegram: @up_hacker                                      
    """)

    while True:
        phone_num = input(Fore.CYAN + "Введите номер телефона: +38" + Style.RESET_ALL)
        try:
            if is_allowed_num(phone_num) is True and len(phone_num) == 10:
                print(Fore.LIGHTGREEN_EX + "Ok.")
                break
            elif len(phone_num) != 10:
                print(Fore.RED + "- Ошибка! Длина номера телефона должна состоять из 10 цифр!")
                continue
            elif is_allowed_num(phone_num) is False:
                print(Fore.RED + "- Ошибка! Допустимы только числа.")
                continue
        except:
            print(Fore.RED + "- Некорректно!")
            continue

    while True:
        name = input(Fore.CYAN + "Имя жертвы (на укр/рус): "+ Style.RESET_ALL)
        try:
            if is_allowed_str(name) is True and len(name) >= 2:
                print(Fore.LIGHTGREEN_EX + "Ok.")
                break
            elif len(name) < 2:
                print(Fore.RED + "- Ошибка! Минимальная длина имени 2 символа!")
                continue
            elif is_allowed_str(name) is False:
                print(Fore.RED + "- Ошибка! Допустимы только русские и украинские буквы, исключены числа.")
                continue
        except:
            print(Fore.RED + "- Некорректно!")
            continue

    while True:
        name_o = input(Fore.CYAN + "Отчество жертвы (не обязательно): " + Style.RESET_ALL)
        try:
            if is_allowed_str(name_o) is True and len(name_o) >= 2:
                print(Fore.LIGHTGREEN_EX + "Ok.")
                break
            elif name_o == '':
                print(Fore.LIGHTGREEN_EX + "Ok.")
                break
            elif len(name_o) < 2:
                print(Fore.RED + "- Ошибка! Минимальна длина имени 2 символа!")
                continue
            elif is_allowed_str(name_o) < 2:
                print(Fore.RED + "- Ошибка! Допустимы только русские и украинские буквы, исключены числа.")
                continue
        except:
            print(Fore.RED + "Некорректно!")

    while True:
        delay = input(Fore.CYAN + "Введите время задержки между запросами (мин. 4): " + Style.RESET_ALL)
        try:
            if int(delay) >= 4 and is_allowed_num(delay) is True:
                print(Fore.LIGHTGREEN_EX + "Ok.")
                break
            elif int(delay) < 4:
                print(Fore.RED + "- Ошибка! Мимимальное время задержки 4с.")
                continue
            elif is_allowed_num(delay) is False:
                print(Fore.RED + "- Ошибка! Допустимы только числа.")
                continue
            elif delay == '':
                print(Fore.RED + "- Ошибка! Не может быть пустым.")
                continue
        except:
            print(Fore.RED + "Некорректно!")
            continue
    print('_______________________________')
    print(Fore.CYAN + '\n| Номер телефона: ', f'+38{phone_num}')
    print(Fore.CYAN + '| Жертва: ', f'{name} {name_o}')
    print(Fore.CYAN + '| Задержка между запросами: ', f'{delay}\n')
    while True:
        repeat = input(Fore.YELLOW + 'Данные верны? (д/н): ' + Style.RESET_ALL)
        if repeat in ('н', 'Н'):
            clear()
            main()
        elif repeat in ('д', 'Д'):
            send_requests_call(str(name.title()), str(phone_num), str(name_o.title()), int(delay))
            break
        else:
            print(Fore.RED + 'Ошибка! Введите корректный ответ.')
    exit()


if __name__ == '__main__':
    clear()
    main()
