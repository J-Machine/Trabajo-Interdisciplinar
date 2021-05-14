from telegram.ext import Updater, CommandHandler


# Devuelve un mensaje cuando se presional el comando start
def start(update, context):
    update.message.reply_text(
        'Bienvenido(a) al Chat de consultas de la Escuela Profesional de Ciencia de la Computación (UNSA)')


if __name__ == '__main__':
    updater = Updater(token='1862455246:AAHDE6lLYMHHYk7-p_rBSgf_L3CYRkO4IYA', use_context=True)
    dp = updater.dispatcher

    # Ciclo para consultar acciones en el chat
    updater.start_polling()
    updater.idle()
