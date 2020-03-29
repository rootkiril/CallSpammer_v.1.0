import os
import re
from service import *
from colorama import Fore


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
    print(Fore.CYAN + """
      _____      _ _  _____                                           
     / ____|    | | |/ ____|      UKRAINE                                     
    | |     __ _| | | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
    | |    / _` | | |\___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
    | |___| (_| | | |____) | |_) | (_| | | | | | | | | | | |  __/ |   
     \_____\__,_|_|_|_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                    v.1.0  | |    telegram: @up_hacker                                     
                           |_|                                        
    """)

    while True:
        phone_num = input(Fore.MAGENTA + "Введите номер телефона +38: ")
        try:
            if is_allowed_num(phone_num) is True:
                if len(phone_num) == 10:
                    print(Fore.LIGHTGREEN_EX + "Ok.")
                    break
                else:
                    print(Fore.LIGHTRED_EX + "Длина номера телефона должна состоять из 10 цифр!")
                    continue
            else:
                print(Fore.LIGHTRED_EX + "Допустимы только числа.")
                continue
        except:
            print(Fore.LIGHTRED_EX + "Номер телефона введен неверно!")
            continue

    while True:
        name = input(Fore.MAGENTA + "Имя жертвы (на укр/рус): ")
        try:
            if is_allowed_str(name) is True:
                if len(name) >= 2:
                    print(Fore.LIGHTGREEN_EX + "Ok.")
                    break
                else:
                    print(Fore.LIGHTRED_EX + "Минимальная длина имени 2 символа!")
                    continue
            else:
                print(Fore.LIGHTRED_EX + "Допустимые только русские и украинские буквы, исключены числа.")
                continue
        except:
            print(Fore.LIGHTRED_EX + "Некоректно!")
            continue

    while True:
        name_o = input(Fore.MAGENTA + "Отчество жертвы (не обязательно): ")
        try:
            if is_allowed_str(name_o) is True:
                if len(name) >= 2:
                    print(Fore.LIGHTGREEN_EX + "Ok.")
                    break
                else:
                    print(Fore.LIGHTRED_EX + "Минимальна длина имени 2 символа!")
                    continue
            elif name_o == '':
                print(Fore.LIGHTGREEN_EX + "Ok.")
                break
            else:
                print(Fore.LIGHTRED_EX + "Допустимые только русские и украинскые буквы, исключены числа.")
                continue
        except:
            print(Fore.LIGHTRED_EX + "Некоректно!")

    while True:
        delay = input(Fore.MAGENTA + "Введите время задержки между запросами (мин. 4): ")
        try:
            delay = int(delay)
            if isinstance(delay, int):
                if delay >= 4:
                    print(Fore.LIGHTGREEN_EX + "Ok. Начнем!")
                    send_requests_call(str(name), str(phone_num), str(name_o), int(delay))
                    break
                else:
                    print(Fore.LIGHTRED_EX + "Нимимальное время задержки 4с.")
                    continue
            else:
                print(Fore.LIGHTRED_EX + "Некоректно!")
        except:
            print(Fore.LIGHTRED_EX + "Некоректно!")
            continue

    print(Fore.GREEN + f"Спам завершился!\nУспешно: {done}.\nНеуспешно: {fail}")


if __name__ == '__main__':
    clear()
    main()