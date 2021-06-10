# BOT TELEGRAM : CONSULTAS EPCC
#-------------------------------

import logging      # Ayuda a ver lo que sucede con el bot y mostrarlo en consola
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

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
    logger.info(f'El usuario {user_Name} ha iniciado(/start) el bot')   # Consola retroalimentación

    # Botones
    btn_contacto = InlineKeyboardButton(
        text='✉️ Contacto de EPCC',
        callback_data="contacto"
    )
    btn_tramites = InlineKeyboardButton(
        text='🎓 Información de trámites',
        callback_data="tramite"
    )

    # Lo que se muestra al ejecutar el comando /start
    update.message.reply_text(
        text=f'Hola {user_Name} ☺️.\nGracias por usar nuestro bot 🤖. '
             f'A continuación te mostramos los tipos de información que podemos darte.\n'
             f'Sólo toca la opción que te interesa.',
        reply_markup=InlineKeyboardMarkup([
            [btn_contacto],
            [btn_tramites]
        ])
    )

def getBotInfo(update, context):
    bot = context.bot
    chat_Id= update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha solicitado información(/infoBot) sobre el bot')

    bot.sendMessage(
        chat_id=chat_Id,
        parse_mode="HTML",
        text=f'Hola soy el bot 🤖 de la <b>Escuela Profesional de Ciencia de la Computación - UNSA</b>.'
             f'Si necesitas información sobre trámites de Bachiller y Título Profesional '
             f'puedo ayudarte. Comienza escribiendo /start.' # 2da manera de responder
    )

# Callbacks functions
def contacto_callback_handler(update, context):
    # print(update.callback_query)
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n'
             '▫️Correo electrónico: epcc@unsa.edu.pe\n'
             '▫️Teléfono: 949107364 (Secretaría Raquel)\n'
             '▫️Horario de atención: Lunes a viernes de 8:30 a 10:30AM (vía Meet) \n'
             '▫ Meet de atención: meet.google.com/smh-igaw-vze\n'
    )

def tramites_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    # Botones
    btn_bachiller = InlineKeyboardButton(
        text=' 🎓📃 Trámite para Bachiller',
        callback_data="bachiller"
    )
    btn_titulacion = InlineKeyboardButton(
        text=' ‍🎓📜‍ Trámite para Titulación',
        callback_data="titulacion"
    )

    query.edit_message_text(
        parse_mode='HTML',
        text=f'{user_Name}, estos son los trámites de los que podemos brindarte información 🙂 ',
        reply_markup=InlineKeyboardMarkup([
            [btn_bachiller],
            [btn_titulacion]
        ])
    )
def titulacion_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Titulacion')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL TITULO PROFESIONAL</b>\n'
             '▫️Solicitud dirigida al Decano de la facultad en formato UNSA.\n'
             '▫️Recibo de pago de expedito para optar el Título Profesional.\n'
             '▫️Trabajo de investigación digitalizado en formato PDF. \n'
             '▫️Constancia emitida por la Biblioteca Virtual de autorización de publicación en el portal de Tesis '
             'Electrónicas. \n'
             '▫️Certificado negativo de antecedentes penales.\n'
             '▫️Certificado oficial de estudios.\n'
             '▫️Copia legalizada de DNI en formato A5. \n'
             '▫️Copia legalizada del Grado de Bachiller. \n'
             '▫️Fotografía tamaño pasaporte a color fondo blanco. \n'
             '▫️Constancia de Egresado. \n'
             '▫️Constancia que acredite dominio de nivel intermedio de idioma extranjero.\n'
             '▫️Constacia de inscripción a SUNEDU del Grado Académico de Bachiller. \n'
             '▫️Constancia de no adeudar Bienes. \n'
             '▫️Constancia de Biblioteca. \n'
             '▫️Recibo de Subdirección de Finanzas de pago de los derechos por todos los conceptos. \n'

    )
def bachiller_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    # Botones
    btn_modo_articulo = InlineKeyboardButton(
        text=' 📃 Modalidad por Artículo Científico',
        callback_data="articulo"
    )
    btn_modo_proyecto = InlineKeyboardButton(
        text=' 📃 Modalidad por Proyecto de Investigación',
        callback_data="proyecto"
    )

    query.edit_message_text(
        parse_mode='HTML',
        text=f'Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
        reply_markup=InlineKeyboardMarkup([
            [btn_modo_articulo],
            [btn_modo_proyecto]
        ])
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

    # Crear el callback handler
    # ConversationHandler define como será la conversación
    dp.add_handler(ConversationHandler(
        entry_points=[
            # Al recibir el patron definido en el data del botón ejecuta la funcion callback
            CallbackQueryHandler(pattern='contacto', callback=contacto_callback_handler),
            CallbackQueryHandler(pattern='tramite', callback=tramites_callback_handler),
            CallbackQueryHandler(pattern='bachiller', callback=bachiller_callback_handler),
            CallbackQueryHandler(pattern='titulacion', callback=titulacion_callback_handler)
        ],
        states={},
        fallbacks=[]
    ))

    # Preguntar por mensajes entrantes to do el tiempo
    updater.start_polling()

    # Terminar bot con ctrl + c
    updater.idle()