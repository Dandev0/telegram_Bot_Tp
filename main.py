import logging
from function import info_user, binding, switch, bot, update_firmware, info_device, update_signal, device_info, check_appid, update_more_device


@bot.message_handler(commands=['help'])
def description(message):
    bot.send_message(message.chat.id, "1) Я могу вывести информацию о пользователях Ujin по номеру телефона. Команда: 1\n2) Могу Привязать\Отвязать устройство от квартиры. Команда: 2\n3)Могу привязать карнизы. Команда: 3\n4)Могу выбирать версию прошивки и обновлять устройства УД.\nВведи команду /button для получения списка.")


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привет {user_id}, {username}, я знаю все про пользоватей Ujin)))')


@bot.callback_query_handler(func=lambda call: True)
def call(call):
    if call.message:
        if call.data == 'item_1':
            logging.warning('Info_user')
            bot.send_message(call.message.chat.id, 'Введите номер телефона: ')
            bot.register_next_step_handler(call.message, callback=info_user)


        if call.data == 'item_2':
            logging.warning('binding')
            bot.send_message(call.message.chat.id,
                             'Введите аппартмент и серийный номер для привязки через запятую\nДля отвязки аппартмент укажите 0: ')
            bot.register_next_step_handler(call.message, callback=binding)


        if call.data == 'item_3':
            logging.warning('switch')
            bot.send_message(call.message.chat.id,
                             'По заказу Андрея\nВведите серийный номер карниза, затем реле(через запятую)')
            bot.register_next_step_handler(call.message, callback=switch)


        if call.data == 'item_4':
            logging.warning('update_firmware')
            bot.send_message(call.message.chat.id,
                             'Введите серийный номер устройства, тип прошивки(стабильная, альфа или бета(через запятую)')
            bot.register_next_step_handler(call.message, callback=update_firmware)


        if call.data == 'item_5':
            logging.warning('info_device')
            bot.send_message(call.message.chat.id,
                             'Введите серийный номер устройства, чтобы получить о нем информацию!)')
            bot.register_next_step_handler(call.message, callback=info_device)


        if call.data == 'item_6':
            logging.warning('update_signal')
            bot.send_message(call.message.chat.id,
                             'Введите серийный номер устройства, имя сигнала, значение\nВсе через запятую и пробел\nДля инвертирования реле введи сигнал: rele-inv')
            bot.register_next_step_handler(call.message, callback=update_signal)


        if call.data == 'item_7':
            logging.warning('device_info')
            bot.send_message(call.message.chat.id,
                             'Введите app_id для получения списка устройств!')
            bot.register_next_step_handler(call.message, callback=device_info)


        if call.data == 'item_8':
            logging.warning('check_appid')
            bot.send_message(call.message.chat.id, 'Введите серийный номер: ')
            bot.register_next_step_handler(call.message, callback=check_appid)

        if call.data == 'item_9':
            logging.warning('update_more_device')
            bot.send_message(call.message.chat.id, 'Отправьте текствоый файл со списком серийных номеров в построчном виде.\nНапример:\n456123324\n4568979 ')
            bot.register_next_step_handler(call.message, callback=update_more_device)


bot.polling(none_stop=True)
