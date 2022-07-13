from django.http import Http404
from django.shortcuts import render, redirect
from backend.CRUD.crud_user import user_create, user_read
from django.contrib import auth
from backend.misc import firebase_init

fauth = firebase_init


# ---------------------
# Authentication
# --------------------
def signUp(request):
	try:
		if (request.session['uid']):
			user_session = fauth.get_account_info(request.session['uid'])
			if (user_session):
				user = user_read(user_session['users'][0]['email'])
				if (user['email'] == "admin_jakun@admin.com" or user['email'] == "mika@mika.com"):
					return render(request, 'signup.html')
	except:
			raise Http404


def postSignUp(request):
	email = request.POST.get("email")
	password = request.POST.get("password1")
	password2 = request.POST.get("password2")
	nama = request.POST.get("nama")
	if (password == password2):
		message = user_create(email, password, nama)
	if message == "":
		return redirect("user:signin")
	else:
		return redirect("user:signup")

def signIn(request):
	return render(request, 'signin.html')

def postSignIn(request):
	email = request.POST.get("email")
	password = request.POST.get("password")
	try:
		user = fauth.sign_in_with_email_and_password(email, password)
		print(user)
		session_id = user['idToken']
		request.session['uid'] = str(session_id)
		print(request.session['uid'])
		return redirect('/')
	except:
		return redirect(signIn)

def logout(request):
	auth.logout(request)
	return redirect("user:signin")
