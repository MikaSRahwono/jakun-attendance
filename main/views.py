from django.shortcuts import render, redirect

from backend.CRUD.crud_attendance import attend_create, absent, attend_read
from django.contrib import auth
from django.http import Http404

from backend.CRUD.crud_jadwal import sbm_read_all, simak_read_all
from backend.CRUD.crud_user import user_read
from backend.constants.jadwal import jadwal_jenis, jadwal_id, dictJadwal
from backend.constants.jurusan import dictJurusan
from backend.misc import firebase_init, custom_qr

fauth = firebase_init

def index(request):
    return redirect("main:form")

# ---------------------
# Authentication
# --------------------
def form(request):
    jadwal_sbm = sbm_read_all()
    jadwal_simak = simak_read_all()
    print(jadwal_sbm)
    return render(request, 'form.html', {
        'jadwal_sbm': jadwal_sbm,
        'jadwal_simak': jadwal_simak
    })

def postForm(request):
    nama = request.POST.get("nama")
    email = request.POST.get("email")
    telephone = request.POST.get("telephone")
    npm = request.POST.get("npm")
    fakultas = request.POST.get("fakultas")
    jurusan = request.POST.get(dictJurusan[fakultas])
    ukuran = request.POST.get("ukuran")
    jalur = request.POST.get("jalur")
    jadwal = request.POST.get(dictJadwal[jalur])

    idJadwal = jadwal_id[jadwal]
    jenisJadwal = jadwal_jenis[jadwal]

    message = attend_create(nama, telephone, email, npm, fakultas, jurusan, ukuran, jalur, jadwal, idJadwal, jenisJadwal)
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
                qr = custom_qr.get_qr("https://jaketkuningui2022.herokuapp.com/detail/"+id)
                print(qr)
                if(data):
                    return render(request, 'details.html', {
                        'nama': user['nama'],
                        'data': data,
                        'qr': qr,
                        'id': id
                    })
                else:
                    raise Http404
    except:
        data = attend_read(id)
        qr = custom_qr.get_qr("https://jaketkuningui2022.herokuapp.com/detail/" + id)
        if(data):
            return render(request, 'details.html', {
                'data': data,
                'id': id,
                'qr': qr,
            })
        else:
            raise Http404


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

def search(request):
    try:
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                return render(request, 'cari.html')
        else:
            raise Http404
    except:
        return redirect('user:signin')

def postsearch(request):
    npm = request.POST.get('npm')
    return redirect('main:detail', id=npm)

def faq(request):
    return render(request, 'faq.html')
