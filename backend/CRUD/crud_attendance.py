import firebase_admin
from firebase_admin import credentials, firestore, storage

from backend.CRUD.crud_jadwal import sbm_updateCounter, simak_updateCounter
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
def attend_create(nama, telepon, email, npm, fakultas, jurusan, ukuran, jalur, jadwal, id_jadwal, jenis_jadwal):
    try:
        data = {
            'nama': nama,
            'telepon': telepon,
            'email': email,
            'npm': npm,
            'fakultas': fakultas,
            'jurusan': jurusan,
            'ukuran': ukuran,
            'link_page': 'https://jaketkuningui2022.herokuapp.com/detail/'+npm,
            'absence': -1,
            'jalur': jalur,
            'jadwal': jadwal,
            'waktu_pengajuan': datetime.datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%c')
        }
        db.collection('attendance').document(npm).set(data)

        print(jenis_jadwal)
        print(id_jadwal)

        if jenis_jadwal == "jadwal_sbm":
            print(11)
            sbm_updateCounter(id_jadwal)
        elif jenis_jadwal == "jadwal_simak":
            print(22)
            simak_updateCounter(id_jadwal)

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

def absent(npm):
    try:
        db.collection('attendance').document(npm).update({
            "absence": 1,
            "waktu_pengambilan": datetime.datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%c')
        })
        return ""
    except:
        return "terjadi error"