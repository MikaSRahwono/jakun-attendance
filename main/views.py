from django.shortcuts import render, redirect

from backend.CRUD.crud_attendance import attend_create, absent, attend_read
from django.contrib import auth

from backend.CRUD.crud_user import user_read
from backend.misc import firebase_init, custom_qr

fauth = firebase_init


# ---------------------
# Authentication
# --------------------
def form(request):
    return render(request, 'form.html')

def postForm(request):
    nama = request.POST.get("nama")
    email = request.POST.get("email")
    telephone = request.POST.get("telephone")
    npm = request.POST.get("npm")
    fakultas = request.POST.get("fakultas")
    jurusan = request.POST.get("jurusan")
    ukuran = request.POST.get("ukuran")

    message = attend_create(nama, telephone, email, npm, fakultas, jurusan, ukuran)
    if (message != "terjadi error"):
        return redirect("detail/" + message)
    else:
        message = "gagal upload"
        return redirect("main:form")

def detail(request, id):
    try:
        print("testing")
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                print(user_session)
                user = user_read(user_session['users'][0]['email'])
                data = attend_read(id)
                qr = custom_qr.get_qr("http://127.0.0.1:8000/absen/"+id)
                print(qr)
                return render(request, 'details.html', {
                    'nama': user['nama'],
                    'data': data,
                    'qr': qr,
                    'id': id
                })
    except:
        data = attend_read(id)
        qr = custom_qr.get_qr("http://127.0.0.1:8000/absen/" + id)
        return render(request, 'details.html', {
            'data': data,
            'id': id,
            'qr': qr,
        })


def absen(request, id):
    try:
        if(request.session["uid"]):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                user = user_read(user_session['users'][0]['email'])
                absent(id, user["nama"])
    except:
        pass
    return redirect('main:detail', id=id)
