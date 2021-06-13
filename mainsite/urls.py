from django.urls import path
from . import views

app_name = 'mainsite'

urlpatterns = [
	path('contact/', views.contact),
	path('login/', views.login_call),
	path('category/', views.category),
	path('logout/', views.logout_call),
	path('barbar/', views.barbar,name="barbar"),
	path('hotel/', views.hotel),
	path('restorent/', views.restorent),
	path('review/', views.review, name="review"),
    path('rating/<int:id>/', views.rating, name="rating"),


]