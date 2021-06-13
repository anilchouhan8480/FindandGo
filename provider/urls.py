from django.urls import path
from . import views

app_name = 'provider'

urlpatterns =  [
	path('register/', views.register),
	path('profile/', views.profile),
	path('edit_profile/', views.edit_profile),

]