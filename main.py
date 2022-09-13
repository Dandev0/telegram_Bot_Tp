import telebot
import requests
from requests import Session

session = Session()


bot = telebot.TeleBot('5321021406:AAGFKeWH3wtTHXs7FVG44WbLLKYs84RAXkk')

proxy = {

    'https': "socks5h//koksharov:G81tKXQE4VQG@46.146.242.247"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

}
session.proxies.update(proxy)

def switch(message):
    try:
        info = message.text
        info = info.split(',')
        serialnumber_c = info[0]
        serialnumber_relay = info[1]
        request = requests.get(
            f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber_relay}&param=tps1&value=3')
        if request.status_code == 200:
            requestt_2 = requests.get(f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber_relay}&param=tps2&value=3')
            if requestt_2.status_code == 200:
                requestt_3 = requests.get(f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber_relay}&param=ss-tbl&value=[{serialnumber_c},1,{serialnumber_c},2]')
                if requestt_3.status_code == 200:
                    bot.send_message(message.chat.id, 'Карниз привязан')
                else:
                    bot.send_message(message.chat.id, f'Ошибка!Статус код: {requestt_3.status_code}')
    except IndexError:
        bot.send_message(message.chat.id, 'Ошибочная форма заполнения')
    except TypeError:
        bot.send_message(message.chat.id, 'Вы что-то сделали не так!')

def binding(message):
    try:

        info = message.text
        info = info.split(',')
        app_id = info[0]
        serialnumber = info[1]
        request = requests.get(f'https://api-product.mysmartflat.ru/api/admin/connect-device-apartment/?apartment={app_id}&serialnumber={serialnumber}')
        if request.status_code == 200:
            bot.send_message(message.chat.id,'Запрос успешно выполнен')
        else:
            bot.send_message(message.chat.id, 'От сервера пришел откат')
    except IndexError:
        bot.send_message(message.chat.id, 'Ошибочная форма заполнения')
    except TypeError:
        bot.send_message(message.chat.id, 'Вы что-то сделали не так!')


def info_user(message):

    number = message.text
    request_info_user = session.get(
            f'https://api-product.mysmartflat.ru/api/script/getuserdatafromphonenumber/?phone={number}', proxies=proxy, headers=headers)
    response = request_info_user
    response = response.json()
    i = 0
    x = 0
    for i in range(len(response)):
        try:
            provider_info = response[i]["provider"]
            user_name = response[i]["data"]["user"]["user_fullname"]
            user_token = response[i]["token"]
            number_info = response[i]["data"]["user"]["user_phone"]
            bot.send_message(message.chat.id, f'Провайдер: {provider_info}\nФио: {user_name}\nТокен: {user_token}\nТелефон: {number_info}')
            try:
                for x in range(len(response[i]["data"]["user"]["apartment"])):
                    adres = response[i]["data"]["user"]["apartment"][x]["title"]
                    appartment_id = response[i]["data"]["user"]["apartment"][x]["id"]
                    sip_info = response[i]["data"]["user"]["apartment"][x]["sip"]
                    complex_id = response[i]["data"]["user"]["apartment"][x]["complex_id"]
                    building_id = response[i]["data"]["user"]["apartment"][x]["building_id"]
                    bot.send_message(message.chat.id, f'Адрес: {adres}\nAppartment_id: {appartment_id}\nSip: {sip_info}\nComplex_id: {complex_id}\nBuilding_id: {building_id}')
                    x += 1

            except IndexError:
                bot.send_message(message.chat.id, "Квартиры для этого аккаунта закончились")
                x = 0

        except KeyError:
            bot.send_message(message.chat.id, 'Нет квартиры')
        except TypeError:
            bot.send_message(message.chat.id, 'Вы что-то сделали не так!')
