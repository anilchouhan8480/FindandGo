from django.shortcuts import render, redirect
from .models import BusinessTypes, BusinessInfo
from django.contrib.auth.models import User
from FindandGo.models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

def register(request):

	bOBj = BusinessTypes.objects.all()


	if request.method == "POST":
		b = request.POST['bname']
		f = request.POST['first']
		l = request.POST['last']
		e = request.POST['email']
		adr = request.POST['address']
		a = request.POST['area']
		c = request.POST['city']
		pin = request.POST['pincode']
		mb = request.POST['phone']
		bimg = request.FILES['b_img']
		st = request.POST['state']
		btype = request.POST['btype']
		un = request.POST['username']
		pwd = request.POST['password']

		u = User(username=un, password=make_password(pwd), first_name=f, last_name=l, email=e)
		u.save()

		tobj = BusinessTypes.objects.get(id=btype)

		# j = BusinessTypes.objects.get(id=id)
		pro_obj = BusinessInfo(business_name=b,mobile=mb,street=adr,user=u,biz_img=bimg,biz_type=tobj,area=a, name=f,email=e,city=c, pincode=pin,state=st)
		pro_obj.save()
			
		messages.success(request, "Congrats! Your have Successfully Created your Business,Now Login For Great Exprience.")
		return redirect('/mainsite/login/')

	return render(request, 'register.html', {'bOBj' : bOBj})


def profile(request):

	bizObj = BusinessInfo.objects.filter(user__username=request.user)

	# uObj = User.objects.filter(username = request.user)


	return render(request, "profile.html", {'bizObj': bizObj})	

def edit_profile(request):

	bizObj = BusinessInfo.objects.filter(user__username=request.user)
	# uObj = User.objects.filter(username = request.user)

	if request.method == "POST":
		a   = request.POST['bname']        
		b   = request.POST['name']
		c   = request.POST['email']
		d   = request.POST['street']
		e   = request.POST['area']
		f   = request.POST['city']
		g   = request.POST['mob']
		h   = request.POST['state']

		bizObj.update(business_name=d, name=b, email=c, street=d, area=e, city=f,mobile=g, state=h)
		# uObj.update(first_name=b, email=c)

		return redirect('/provider/profile/')

	return render(request, "edit_profile.html",{'bizObj': bizObj})


