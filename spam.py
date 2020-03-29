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
            if is_allowed_num(phone_num) is True:
                if len(phone_num) == 10:
                    print(Fore.LIGHTGREEN_EX + "Ok.")
                    break
                else:
                    print(Fore.RED + "- Ошибка! Длина номера телефона должна состоять из 10 цифр!")
                    continue
            else:
                print(Fore.RED + "- Ошибка! Допустимы только числа.")
                continue
        except:
            print(Fore.RED + "- Ошибка! Номер телефона введен неверно!")
            continue

    while True:
        name = input(Fore.CYAN + "Имя жертвы (на укр/рус): "+ Style.RESET_ALL)
        try:
            if is_allowed_str(name) is True:
                if len(name) >= 2:
                    print(Fore.LIGHTGREEN_EX + "Ok.")
                    break
                else:
                    print(Fore.RED + "- Ошибка! Минимальная длина имени 2 символа!")
                    continue
            else:
                print(Fore.RED + "- Ошибка! Допустимые только русские и украинские буквы, исключены числа.")
                continue
        except:
            print(Fore.RED + "- Некоректно!")
            continue

    while True:
        name_o = input(Fore.CYAN + "Отчество жертвы (не обязательно): "+ Style.RESET_ALL)
        try:
            if is_allowed_str(name_o) is True:
                if len(name) >= 2:
                    print(Fore.LIGHTGREEN_EX + "Ok.")
                    break
                else:
                    print(Fore.RED + "- Ошибка! Минимальна длина имени 2 символа!")
                    continue
            elif name_o == '':
                print(Fore.LIGHTGREEN_EX + "Ok.")
                break
            else:
                print(Fore.RED + "- Ошибка! Допустимы только русские и украинскые буквы, исключены числа.")
                continue
        except:
            print(Fore.RED + "Некоректно!")

    while True:
        delay = input(Fore.CYAN + "Введите время задержки между запросами (мин. 4): " + Style.RESET_ALL)
        try:
            delay = int(delay)
            if isinstance(delay, int):
                if delay >= 4:
                    break
                else:
                    print(Fore.RED + "- Ошибка! Мимимальное время задержки 4с.")
                    continue
            else:
                print(Fore.RED + "Некоректно!")
        except:
            print(Fore.RED + "Некоректно!")
            continue
    send_requests_call(str(name.title()), str(phone_num), str(name_o.title()), int(delay))


if __name__ == '__main__':
    clear()
    main()