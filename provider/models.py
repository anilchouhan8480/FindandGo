from django.db import models
from FindandGo.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.


class BusinessTypes(models.Model):
	bus_Name = models.CharField(max_length=50)

class BusinessInfo(models.Model):
	business_name = models.CharField(max_length = 100)
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	street = models.CharField(max_length = 200)	
	area = models.CharField(max_length = 100)
	city = models.CharField(max_length = 50)
	pincode = models.IntegerField()
	mobile = models.CharField(max_length=100, default=0)
	biz_img = models.ImageField(upload_to="business_images", blank=True)
	biz_type = models.ForeignKey(BusinessTypes, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	state = models.CharField(max_length = 100)
	dated = models.DateTimeField(auto_now=True)