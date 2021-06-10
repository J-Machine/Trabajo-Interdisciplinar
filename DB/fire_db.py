import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# SETUP: Usar las credenciales por defecto de la aplicación

cred = credentials.Certificate("/home/howl/LAB/TI/Telegram-Bot/Doc/service-account-file.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

# Crear DOCUMENTOS:
requisitos_bachiller = {
    'id': 1, 'req': 'Solicitud dirigida al Decano de la Facultad (considerar correo institucional y personal)',
    'id': 2, 'req': 'Solicitud dirigida al Decano de la Facultad (considerar correo institucional y personal)',
    'id': 2, 'req': 'Caratula del Trabajo de Investigación',
    'id': 3, 'req': 'Copia de Certificados de Estudio Original',
    'id': 4, 'req': 'Copia del Diploma de Bachiller',
    'id': 5, 'req': 'Copia de Antecedentes Penales',
    'id': 6, 'req': 'Copia del DNI actualizado',
    'id': 7, 'req': 'Constancia de No Adeudar Material Bibliográfico (DUFA)',
    'id': 8, 'req': 'Constancia de No Adeudar Bienes a la Facultad (declaración jurada + pago de S/. 10.00 soles)',
    'id': 9, 'req': 'Recibo de Pago de derecho de Título profesional S/. 533.00',
    'id': 10, 'req': 'Recibo de Tramite S/. 6.00',
    'id': 11,
     'req': '2 Fotografías recientes de frente tamaño pasaporte a colores con fondo blanco digitalizado en Formato '
            'JPG, con terno azul que cumplan las características publicadas en la página web de la UNSA ('
            'Repositorio).',
    'id': 12, 'req': 'Trabajo de Investigación digitalizado en formato PDF 3 ejemplares.'
}
req_bachiller = db.collection(u'tramite-bachiller').document(u'requisitos')
req_bachiller.set(requisitos_bachiller)
