import os
import re
from service import *


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def is_allowed(string):
    char_regex = re.compile(r'[^а-яА-ЯєіїЄІЇ]')
    string = char_regex.search(string)
    return not bool(string)


def main():
    print("""
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
        phone_num = input("Введите номер телефона +38: ")
        try:
            phone_num = int(phone_num)
            if isinstance(phone_num, int):
                if len(str(phone_num)) == 9:
                    phone_num = str(phone_num)
                    print("Ok.")
                    break
                else:
                    print("Длина номера телефона должна состоять из 10 цифр!")
                    continue
        except:
            print("Номер телефона введен неверно!")
            continue

    while True:
        name = input("Имя жертвы (на укр/рус): ")
        try:
            if is_allowed(name) is True:
                if len(name) > 2:
                    print("Ok.")
                    break
                else:
                    print("Минимальная длина имени 3 символа!")
                    continue
            else:
                print("Допустимые только русские и украинские буквы, исключены числа.")
                continue
        except:
            print("Некоректно!")
            continue

    while True:
        name_o = input("Отчество жертвы (не обязательно): ")
        try:
            if is_allowed(name_o) is True:
                if len(name) > 2:
                    print("Ok.")
                    break
                else:
                    print("Минимальна длина имени 2 символа!")
                    continue
            if name_o == '':
                print("Ok.")
                break
            else:
                print("Допустимые только русские и украинскые буквы, исключены числа.")
                continue
        except:
            print("Некоректно!")

    while True:
        delay = input("Введите время задержки между запросами (мин. 4): ")
        try:
            delay = int(delay)
            if isinstance(delay, int):
                if delay < 4:
                    delay = str(delay)
                    print("Ok. Начнем!")
                    # send_requests_call(name, phone_num, delay, name_o)
                    break
                else:
                    print("Нимимальное время задержки 4с.")
                    continue
            if delay == '':
                print("Ok. Начнем!")
                # send_requests_call(name, phone_num, delay, name_o)
                break
        except:
            print("Некоректно!")
            continue
    print(f"Спам завершился!\nУспешно: {done}.\nНеуспешно: {fail}")


# name_o = input("Отчество жертвы (не обязательно): ")
# print("Хорошо, начнем!")
# send_requests_call(name, phone_num, delay)
# print("Отправка запросов для звонка успешно окончена, ждите звонков!")


if __name__ == '__main__':
    clear()
    main()