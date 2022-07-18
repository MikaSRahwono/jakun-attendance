import firebase_admin
from firebase_admin import credentials, firestore, storage

from backend.misc import firebase_init
import datetime
import pytz

# --------------------------
# Initialize Firebase Admin
# --------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate("testing-key.json")
    firebase_admin.initialize_app(cred)

fauth = firebase_init
db = firestore.client()


# --------------------------
# CRUD Functions
# --------------------------
def sbm_read_all():
    try:
        data_dict = []
        datas = db.collection('jadwal_sbm').where('quota', '>', 0).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

def simak_read_all():
    try:
        data_dict = []
        datas = db.collection('jadwal_simak').where('quota', '>', 0).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

def sbm_updateCounter(tanggal):
    data = db.collection('jadwal_sbm').document(tanggal).get().to_dict()
    data['quota'] -= 1
    db.collection('jadwal_sbm').document(tanggal).set(data)

def simak_updateCounter(tanggal):
    data = db.collection('jadwal_simak').document(tanggal).get().to_dict()
    data['quota'] -= 1
    db.collection('jadwal_simak').document(tanggal).set(data)

