from function import info_user, binding, switch, bot, update_firmware


@bot.message_handler(commands=['help'])
def description(message):
    bot.send_message(message.chat.id, "1) Я могу вывести информацию о пользователях Ujin по номеру телефона. Команда: /1\n2) Могу Привязать\Отвязать устройство от квартиры. Команда: /2\n3)Могу привязать карнизы. Команда: /3")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет ' + message.from_user.first_name + ', я знаю все про пользоватей Ujin)))')


@bot.message_handler(commands=['1'])
def qwe(message):
    bot.send_message(message.chat.id, 'Введите номер телефона: ')
    bot.register_next_step_handler(message, callback=info_user)

@bot.message_handler(commands=['2'])
def bind(message):
    bot.send_message(message.chat.id, 'Введите аппартмент и серийный номер для привязки через запятую\nДля отвязки аппартмент укажите 0: ')
    bot.register_next_step_handler(message, callback=binding)

@bot.message_handler(commands=['3'])
def bind(message):
    bot.send_message(message.chat.id, 'По заказу Андрея\nВведите серийный номер карниза, затем реле(через запятую)')
    bot.register_next_step_handler(message, callback=switch)


@bot.message_handler(commands=['4'])
def bind(message):
    bot.send_message(message.chat.id, 'Введите серийный номер устройства, тип прошивки(стабильная, альфа или бета')
    bot.register_next_step_handler(message, callback=update_firmware)

bot.polling(none_stop=True)
