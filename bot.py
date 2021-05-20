import logging      # Ayuda a ver lo que sucede con el bot y mostrarlo en consola

import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, callbackqueryhandler, conversationhandler, MessageHandler, Filters

# Variables
TOKEN = '1862455246:AAHDE6lLYMHHYk7-p_rBSgf_L3CYRkO4IYA'

# Configuracion de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

# Funciones para comandos
def start(update, context):
    bot = context.bot
    # chat_Id = update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha iniciado(/start) el bot')   # Consola

    # Botones
    btn_contacto = InlineKeyboardButton(
        text='Información de contacto',
        callback_data="contacto"
    )
    btn_tramites = InlineKeyboardButton(
        text='Información de trámites',
        callback_data="tramite"
    )

    # Lo que se muestra en 
    update.message.reply_text(
        text=f'Hola {user_Name}.\nGracias por usar nuestro bot. '
             f'A continuación te mostramos las funciones que  puedes usar',
        reply_markup=InlineKeyboardMarkup([
            [btn_contacto],
            [btn_tramites]
        ])
    )

def getBotInfo(update, context):
    bot = context.bot
    chat_Id= update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha solicitado información sobre el bot')
    bot.sendMessage(
        chat_id=chat_Id,
        parse_mode="HTML",
        text=f'Hola soy el bot de la <b>Escuela Profesional de Ciencia de la Computación - UNSA</b>' # 2da manera de responder
    )

# Main Function
if __name__ == '__main__':
    mybot = telegram.Bot(token=TOKEN)
    print(mybot.getMe())  # Muestra en consola información sobre el bot

    # Updater: se conecta y recibe los mensajes
    updater = Updater(mybot.token, use_context=True)

    # Crear el 'despachador'
    dp = updater.dispatcher

    # Crear comando y el método (acción del comando)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("botInfo", getBotInfo))

    # Preguntar por mensajes entrantes
    updater.start_polling()

    # Terminar bot con ctrl + c
    updater.idle()