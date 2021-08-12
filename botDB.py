import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# ### INICIANDO CONEXIÓN CON FIREBASE
# Importando sdk de firebase
cred = credentials.Certificate("firebase_sdk.json")

# Referencia a la BD en tiempo real de FireBase
firebase_admin.initialize_app(cred, {'databaseURL': 'https://epcc-telegram-bot-default-rtdb.firebaseio.com/'})

# ### LECTURA DE BASE DE INFORMACIÓN EN BASE DE DATOS ###
# Referencia a estructura de DataBase
ref_DB = db.reference('/')
bot_DB = ref_DB.get()  # return dict type

list_child_DB = list(bot_DB)  # Hijos de root
main_nodo = list_child_DB[0]  # key del 1er nodo donde se almacena la informacion a mostrar en el bot


# ### Funciones para obtener los datos de Firebase
def select_list_info(tramite):
    """ Devuelve la lista de:
        0: contacto,
        1: bachiller automatico,
        2: bachiller trabajo investigacion,
        3: titulo trabajo investigacion,
        4: titulo suficiencia"""
    if tramite == 0:
        ref_contacto = db.reference(main_nodo + '/Contacto')
        print("Creando lista de info Contacto")
        return ref_contacto.get()  # return a list type
    elif tramite == 1:
        ref_bach_auto = db.reference(main_nodo + '/Bachiller-Automatico')
        print("Creando lista de info Bachiller Automático")
        return ref_bach_auto.get()  # return a list type
    elif tramite == 2:
        ref_bach_ti = db.reference(main_nodo + '/Bachiller-TI')
        print("Creando lista de info Bachiller Trabajo investigacion")
        return ref_bach_ti.get()  # return a list type
    elif tramite == 3:
        ref_titulo_ti = db.reference(main_nodo + '/Titulo-TI')
        print("Creando lista de info Titulo Trabajo de investigación")
        return ref_titulo_ti.get()  # return a list type
    elif tramite == 4:
        ref_titulo_suf = db.reference(main_nodo + '/Titulo-suficiencia')
        print("Creando lista de info Titulo suficiencia")
        return ref_titulo_suf.get()  # return a list type

# Parse datos a String
# ----------------------
def print_info_contact(list_contact):
    print('Actualizando información de contacto')
    string_info = ''
    for row in list_contact:
        if isinstance(row, dict):
            string_info += '▫️<b>' + row['Tipo Informacion'] + ':</b> ' + row['Información'] + '\n'
    return string_info

def print_info_requisitos(list_with_info):
    print('Actualizando requisitos')
    string_info = ''
    for row in list_with_info:
        if isinstance(row, dict):
            string_info += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'
    return string_info
