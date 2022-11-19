#########################################################
from config import bot
import config
from time import sleep
import re
#########################################################
# Aquí vendrá la implementación de la lógica del bot


@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "Hola, soy un \U0001F916, ¿cómo estás?",
        parse_mode="Markdown")


@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    response = (
        "Estos son los comandos y órdenes disponibles:\n"
        "\n"
        "*/start* - Inicia la interacción con el bot\n"
        "*/help* - Muestra este mensaje de ayuda\n"
        "*sumar {valor1} y {valor2}* - Calcula la suma de dos valores\n"
        "*restar {valor1} y {valor2}* - Calcula la resta de dos valores\n"
        "*multiplicar {valor1} y {valor2}* - Calcula la multiplicación de dos valores\n"
        "*dividir {valor1} y {valor2}* - Calcula la división de dos valores\n"
    )
    bot.send_message(
        message.chat.id,
        response,
        parse_mode="Markdown")


@bot.message_handler(
    regexp=r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_add(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    parts = re.match(
        r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)",
        message.text,
        flags=re.IGNORECASE)
    print(parts)
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    result = oper1 + oper2
    bot.reply_to(
        message,
        f"\U0001F522 Resultado: {result}")


@bot.message_handler(
    regexp=r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_add(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    parts = re.match(
        r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)",
        message.text,
        flags=re.IGNORECASE)
    print(parts[0])
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    if oper1 != 0 and oper2 != 0:
        result = oper1 / oper2
        bot.reply_to(
            message,
            f"\U0001F522 Resultado: {result}")
    else:
        bot.reply_to(
            message,
            f"\U0001F522 no debe incluir 0 ")


@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    mes = "\U0001F63F Ups, no entendí lo que me dijiste."
    sleep(len(mes))
    bot.reply_to(
        message,
        mes)


#########################################################
if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################
