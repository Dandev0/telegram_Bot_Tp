import logging
import time
import telebot
import requests
from telebot import types

bot = telebot.TeleBot('5321021406:AAGFKeWH3wtTHXs7FVG44WbLLKYs84RAXkk')


@bot.message_handler(commands='button')
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item_1 = types.InlineKeyboardButton('Инфо о пользователе', callback_data='item_1' )
    item_2 = types.InlineKeyboardButton('Привязка/Отвязка',callback_data='item_2')
    item_3 = types.InlineKeyboardButton('Карнизы', callback_data='item_3')
    item_4 = types.InlineKeyboardButton('Прошивка устройства', callback_data='item_4')
    item_5 = types.InlineKeyboardButton('Информация о устройстве', callback_data='item_5')
    item_6 = types.InlineKeyboardButton('Обновить сигнал', callback_data='item_6')
    markup.add(item_1, item_2, item_3, item_4, item_5, item_6)
    bot.send_message(message.chat.id, 'Выбери команду: ', reply_markup=markup)

def switch(message):
    try:
        info = message.text
        info = info.split(', ')
        serialnumber_c = info[0]
        serialnumber_relay = info[1]
        request = requests.get(
            f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber_relay}&param=tps1&value=3')
        if request.status_code == 200:
            time.sleep(.5)
            requestt_2 = requests.get(
                f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber_relay}&param=tps2&value=3')
            if requestt_2.status_code == 200:
                time.sleep(.5)
                requestt_3 = requests.get(
                    f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber_relay}&param=ss-tbl&value=[{serialnumber_c},1,{serialnumber_c},2]')
                if requestt_3.status_code == 200:
                    bot.send_message(message.chat.id, 'Карниз привязан')
                else:
                    bot.send_message(message.chat.id, f'Ошибка!Статус код: {requestt_3.status_code}')
    except IndexError:
        bot.send_message(message.chat.id, 'Ошибочная форма заполнения')
    except TypeError:
        bot.send_message(message.chat.id, 'Вы что-то сделали не так!')
    restart_button(message)


def binding(message):
    try:
        info = message.text
        info = info.split(', ')
        app_id = info[0]
        serialnumber = info[1]
        request = requests.get(
            f'https://api-product.mysmartflat.ru/api/admin/connect-device-apartment/?apartment={app_id}&serialnumber={serialnumber}')
        request = request.json()
        if request["error"] == 0:
            bot.send_message(message.chat.id, 'Запрос успешно выполнен!')
        else:
            bot.send_message(message.chat.id, 'От сервера пришел откат')
    except IndexError:
        bot.send_message(message.chat.id, 'Ошибочная форма заполнения')
    except TypeError:
        bot.send_message(message.chat.id, 'Вы что-то сделали не так!')
    restart_button(message)
def info_user(message):
    try:
        number = message.text
        request_info_user = requests.get(
            f'https://api-product.mysmartflat.ru/api/script/getuserdatafromphonenumber/?phone={number}')
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
                bot.send_message(message.chat.id,
                                 f'Провайдер: {provider_info}\nФио: {user_name}\nТокен: {user_token}\nТелефон: {number_info}')
                try:
                    for x in range(len(response[i]["data"]["user"]["apartment"])):
                        adres = response[i]["data"]["user"]["apartment"][x]["title"]
                        appartment_id = response[i]["data"]["user"]["apartment"][x]["id"]
                        sip_info = response[i]["data"]["user"]["apartment"][x]["sip"]
                        complex_id = response[i]["data"]["user"]["apartment"][x]["complex_id"]
                        building_id = response[i]["data"]["user"]["apartment"][x]["building_id"]
                        bot.send_message(message.chat.id,
                                         f'Адрес: {adres}\nAppartment_id: {appartment_id}\nSip: {sip_info}\nComplex_id: {complex_id}\nBuilding_id: {building_id}')
                        x += 1

                except IndexError:
                    bot.send_message(message.chat.id, "Квартиры для этого аккаунта закончились")
                    x = 0

            except KeyError:
                bot.send_message(message.chat.id, 'Нет квартиры')
            except TypeError:
                bot.send_message(message.chat.id, 'Вы что-то сделали не так!')
    except TypeError:
        bot.send_message(message.chat.id, 'Отвалился VPN на моем сервере или вы ввели не валидный номер!')
    restart_button(message)

def update_firmware(message):
    try:
        info = message.text
        info = info.split(', ')
        serialnumber = info[0]
        type_firmware = info[1]
        if type_firmware == 'Альфа':
            request_set_type_firmware_1 = requests.get(
                f'https://api-product.mysmartflat.ru/api/admin/update-device-config/?serialnumber={serialnumber}&param=device_firmware_alfa_update&value=true')
            time.sleep(1)
            bot.send_message(message.chat.id, 'Принято Альфа!')
            req = request_set_type_firmware_1.json()
            if req['error'] == 0:
                request_auto_update = requests.get(
                    f'https://api-product.mysmartflat.ru/api/admin/update-device-config/?serialnumber={serialnumber}&param=device_firmware_autoupdate&value=true')
                if request_auto_update.status_code == 200:
                    time.sleep(.5)
                    request_update_1 = requests.get(
                    f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber}&param=reset&value=1')
                    if request_update_1.status_code == 200:
                        bot.send_message(message.chat.id, 'Команда на обновление отправлена!\nУстройство не обновится, если оно было не на связи!')

        if type_firmware == 'Бета':
            bot.send_message(message.chat.id, 'Принято Бета!')
            request_set_type_firmware_2 = requests.get(
                f'https://api-product.mysmartflat.ru/api/admin/update-device-config/?serialnumber={serialnumber}&param=device_firmware_beta_update&value=true')
            time.sleep(1)
            req = request_set_type_firmware_2.json()
            if req['error'] == 0:
                request_auto_update = requests.get(
                    f'https://api-product.mysmartflat.ru/api/admin/update-device-config/?serialnumber={serialnumber}&param=device_firmware_autoupdate&value=true')
                if request_auto_update.status_code == 200:
                    time.sleep(.5)
                    request_update_2 = requests.get(
                        f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber}&param=reset&value=1')
                    if request_update_2.status_code == 200:
                        bot.send_message(message.chat.id, 'Команда на обновление отправлена!\nУстройство не обновится, если оно было не на связи!')

        if type_firmware == 'Стабильная':
            bot.send_message(message.chat.id, 'Принято Стабильная!')
            request_set_type_firmware_3 = requests.get(
                f'https://api-product.mysmartflat.ru/api/admin/update-device-config/?serialnumber={serialnumber}&param=device_firmware_stable_update&value=true')
            time.sleep(1)
            req = request_set_type_firmware_3.json()
            if req['error'] == 0:
                request_auto_update = requests.get(f'https://api-product.mysmartflat.ru/api/admin/update-device-config/?serialnumber={serialnumber}&param=device_firmware_autoupdate&value=true')
                if request_auto_update.status_code == 200:
                    time.sleep(.5)
                    request_update = requests.get(
                        f'https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber}&param=reset&value=1')
                    if request_update.status_code == 200:
                        bot.send_message(message.chat.id, 'Команда на обновление отправлена!\nУстройство не обновится, если оно было не на связи!')
    except KeyError:
        bot.send_message(message.chat.id, 'Что-то пошло не так! Проверьте корректность запроса и повторите его')

    except TypeError:
        bot.send_message(message.chat.id, 'Что-то пошло не так! Проверьте корректность запроса и повторите его')
    except IndexError:
        bot.send_message(message.chat.id, 'Что-то пошло не так! Проверьте корректность запроса и повторите его')
    restart_button(message)

def info_device(message):
    try:
        info = message.text
        info = info[0]
        req = requests.get(f'https://api-product-reserved-2.mysmartflat.ru/api/admin/get-signals/?serialnumber={info}')
        logging.warning('запрос ушел')
        if req.status_code == 200:
            req = req.json()
            error = req['error']
            name_signal = req['data']
            try:
                if error == 0:
                    for i in name_signal:
                        bot.send_message(message.chat.id, f"Сигнал: {i['name']}\nНазвание: {i['title']}\nЗначение: {i['value']}")
                else:
                    bot.send_message(message.chat.id, f"Error: {error}")
            except KeyError:
                bot.send_message(message.chat.id, f'Кривой ответ сервера')
        else:
            bot.send_message(message.chat.id, "Статус код != 200")
    except KeyError:
        bot.send_message(message.chat.id, 'Вы ввели не корректный запрос!')
    restart_button(message)
def update_signal(message):
    try:
        info = message.text
        info = info.split(', ')
        serialnumber = info[0]
        signal = info[1]
        value = info[2]
        req = requests.get(f"https://api-product.mysmartflat.ru/api/admin/update-signal/?serialnumber={serialnumber}&param={signal}&value={value}")
        if req.status_code == 200:
            bot.send_message(message.chat.id, f'Значение ({value}) для устройства {serialnumber} установлено\nА может и нет(если устройство было не на связи)')
        else:
            bot.send_message(message.chat.id, "Ответ сервера != 200")

    except KeyError:
        bot.send_message(message.chat.id, 'Вы ввели не корректный запрос!')
    except IndexError:
        bot.send_message(message.chat.id, 'Вы ввели не корректный запрос!')

    time.sleep(.5)
    restart_button(message)



def restart_button(message):
    try:
        bot.send_message(message.chat.id, button(message))
    except:
        pass
