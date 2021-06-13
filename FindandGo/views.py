from django.shortcuts import render, redirect
# from django.http import HttpResponse

def home(request):
	return render(request, 'index.html')

def home2(request):
	return render(request, 'index2.html')