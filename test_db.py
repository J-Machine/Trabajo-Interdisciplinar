import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
# Importando sdk de firebase
cred = credentials.Certificate("firebase_sdk.json")

# Referencia a la BD en tiempo real de FireBase
firebase_admin.initialize_app(cred, {'databaseURL': 'https://epcc-telegram-bot-default-rtdb.firebaseio.com/'})

# ### LECTURA DE BASE DE INFORMACIÓN EN BASE DE DATOS ###
# --- Referencia a estructura de DataBase ---
ref_DB = db.reference('/')
bot_DB = ref_DB.get()
print(type(ref_DB.get()))
print(ref_DB.get())

list_child_DB = list(bot_DB)                   # Hijos de root
main_nodo = list_child_DB[0]                    # key del 1er nodo donde se almacena la informacion a mostrar en el bot

print('REQUISITOS bachiller\n')
ref_bachiller_automatico = db.reference(main_nodo + '/Bachiller-Automatico')
req_bach_auto = ref_bachiller_automatico.get()      # return a list type

print(req_bach_auto)
for row_req in req_bach_auto:
    if isinstance(row_req, dict):
       print( str(row_req['Id']) + '. ' + row_req['Requisito'])

# print(req_bach_auto[1]['Requisito'])


# Obtener nodos iniciales de la base de datos



# Creacion de una coleccion para los datos de contacto
""" 
ref_contact.push({
'Email': 'epcc@unsa.edu.pe',
'Telefono': '949107364 (Secretaría Raquel)',
'Horario': 'Lunes a viernes de 8:30 a 10:30AM (vía Meet) ',
'Meet': 'meet.google.com/smh-igaw-vze'
})
"""
# Modificacion de varios datos por clave dinamica
contact_node = '-Me7UrfCrKlFFBt24OXv'
"""
ref_contact.update({
    contact_node + '/Email': 'sin correo',
    contact_node + '/Meet': 'https://meet.google.com/smh-igaw-vze'
})
"""
