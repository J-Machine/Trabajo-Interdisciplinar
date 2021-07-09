import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# importando sdk de firebase
cred = credentials.Certificate("epcc-telegram-bot-firebase-adminsdk-bhg3g-a4eb58ca5c.json")

# Referencia a la BD en tiempo real de FireBase
firebase_admin.initialize_app(cred, {'databaseURL': 'https://epcc-telegram-bot-default-rtdb.firebaseio.com/'})

# Referencia a nodo Contacto de la BD
ref_contact = db.reference('/Contacto')

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
