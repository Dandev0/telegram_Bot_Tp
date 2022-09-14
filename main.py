from function import info_user, binding, switch, bot, update_firmware
from telebot import types


@bot.message_handler(commands=['help'])
def description(message):
    bot.send_message(message.chat.id, "1) Я могу вывести информацию о пользователях Ujin по номеру телефона. Команда: 1\n2) Могу Привязать\Отвязать устройство от квартиры. Команда: 2\n3)Могу привязать карнизы. Команда: 3\n4)Могу выбирать версию прошивки и обновлять устройства УД.\nВведи команду /button для получения списка.")


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привет {user_id}, {username}, я знаю все про пользоватей Ujin)))')


@bot.message_handler(commands='button')
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item_1 = types.InlineKeyboardButton('Инфо о пользователе', callback_data='item_1' )
    item_2 = types.InlineKeyboardButton('Привязка/Отвязка',callback_data='item_2')
    item_3 = types.InlineKeyboardButton('Карнизы', callback_data='item_3')
    item_4 = types.InlineKeyboardButton('Прошивка устройства', callback_data='item_4')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id, 'Выбери команду: ', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def call(call):
    if call.message:
        if call.data == 'item_1':
            bot.send_message(call.message.chat.id, 'Введите номер телефона: ')
            bot.register_next_step_handler(call.message, callback=info_user)
        if call.data == 'item_2':
            bot.send_message(call.message.chat.id,
                             'Введите аппартмент и серийный номер для привязки через запятую\nДля отвязки аппартмент укажите 0: ')
            bot.register_next_step_handler(call.message, callback=binding)
        if call.data == 'item_3':
            bot.send_message(call.message.chat.id,
                             'По заказу Андрея\nВведите серийный номер карниза, затем реле(через запятую)')
            bot.register_next_step_handler(call.message, callback=switch)
        if call.data == 'item_4':
            bot.send_message(call.message.chat.id,
                             'Введите серийный номер устройства, тип прошивки(стабильная, альфа или бета(через запятую)')
            bot.register_next_step_handler(call.message, callback=update_firmware)

bot.polling(none_stop=True)
