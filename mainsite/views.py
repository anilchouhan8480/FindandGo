from django.shortcuts import render, redirect
from FindandGo.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from provider.models import BusinessInfo, BusinessTypes
from .models import Contact, Review
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.



def login_call(request):

	if request.method == "POST":
		h = request.POST['username']
		i = request.POST['pwd']

		user = authenticate(username=h, password=i)	

		if user:
			login(request, user)

			messages.success(request,'Login Suucess! Welcome In FindandGo')
			return redirect('/home/')
		else:
			messages.error(request,'username or password not correct')
			return redirect('/mainsite/login/')
			
	return render(request, 'login.html')


def logout_call(request):
    logout(request)
    return redirect('/home/')	


def contact(request):

	if request.method == "POST":
		a = request.POST['name']
		b = request.POST['email']
		c = request.POST['msg']

		Cobj = Contact(name=a, email=b, message=c)
		Cobj.save()


		messages.success(request, "Your Message has been send Successfully, Thanks For Contact.")
		return redirect('/mainsite/contact/')

	return render(request, 'contact.html')
		

def category(request):

	return render(request, 'category.html')

def barbar(request):

	bOBj = BusinessInfo.objects.filter(biz_type_id=1)

	return render(request, 'barbar.html',  {'bOBj' : bOBj})

def hotel(request):

	hOBj = BusinessInfo.objects.filter(biz_type_id=2)
	
	return render(request, 'hotel.html' ,  {'hOBj' : hOBj})

def restorent(request):
	rOBj = BusinessInfo.objects.filter(biz_type_id=3)

	return render(request, 'restorent.html' ,  {'rOBj' : rOBj})		

def review(request):

	Bobj = BusinessInfo.objects.all()

	# if request.method == "POST":
	# 	a   = request.POST['rating']        
	# 	b   = request.POST['msg']

	# 	uObj = User.objects.get(username = request.user)
	# 	bizobj = BusinessInfo.objects.get(id=id)


	# 	rv = Review(score=a, message=b, biz_info_id=bizobj, user_id=uObj)
	# 	rv.save()

	# elif request.method == "GET":
	
	# 	return render(request, 'review.html', {'Bobj':Bobj})


	return render(request, 'review.html', {'Bobj':Bobj})			


def rating(request, id):
		if request.method == "POST":
			a   = request.POST['rating']        
			b   = request.POST['msg']

			uObj = User.objects.get(username = request.user)
			bizobj = BusinessInfo.objects.get(id=id)


			rv = Review(score=a, message=b, biz_info_id=bizobj, user_id=uObj)
			rv.save()
			return redirect('/mainsite/review/')	