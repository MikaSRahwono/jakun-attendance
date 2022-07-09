import firebase_admin
from firebase_admin import credentials, firestore, storage

from backend.misc import firebase_init
import datetime

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
def attend_create(nama, telepon, email, npm, fakultas, jurusan, ukuran):
    try:
        data = {
            'nama': nama,
            'telepon': telepon,
            'email': email,
            'npm': npm,
            'fakultas': fakultas,
            'jurusan': jurusan,
            'ukuran': ukuran,
            'absence': -1,
            'waktu_pengajuan': datetime.datetime.now()
        }
        db.collection('attendance').document(npm).set(data)

        return npm
    except:
        return "terjadi error"

def attend_read(npm):
    try:
        data = db.collection('attendance').document(npm).get().to_dict()
        return data
    except:
        data = []
    return data

def absent(npm, nama):
    try:
        db.collection('attendance').document(npm).update({
            "absence": 1,
            "pengabsen": nama
        })
        return ""
    except:
        return "terjadi error"