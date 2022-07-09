import firebase_admin
from firebase_admin import credentials, firestore, storage, auth

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
# CRUD Functions Authentication
# --------------------------
def user_create(email, password, nama) :
    try:
        user = auth.create_user(email=email, email_verified=False, password=password)
        print('Sucessfully created new user: {0}'.format(user.uid))
    except auth.EmailAlreadyExistsError:
        message = 'The user with the provided email already exists'
        return message;
    except auth.UidAlreadyExistsError:
        message = 'The user with the provided username already exists'
        return message;
    data = {
        'email': email,
        'nama': nama,
    }
    db.collection('users').document(email).set(data)
    return "";

def user_read(email):
    data = db.collection('users').document(email).get().to_dict()
    print(data)
    return data