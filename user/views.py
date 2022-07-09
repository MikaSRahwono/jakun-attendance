from django.shortcuts import render, redirect
from backend.CRUD.crud_user import user_create
from django.contrib import auth
from backend.misc import firebase_init

fauth = firebase_init


# ---------------------
# Authentication
# --------------------
def signUp(request):
	return render(request, 'signup.html')

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
	except:
		return redirect(signIn)
	print(user)
	session_id = user['idToken']
	request.session['uid'] = str(session_id)
	print(request.session['uid'])
	return redirect('/')

def logout(request):
	auth.logout(request)
	return redirect("user:signin")
