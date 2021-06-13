from django.db import models
from provider.models import BusinessTypes, BusinessInfo
from django.contrib.auth.models import User
from FindandGo.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	message = models.TextField(max_length=800)


class Review(models.Model):
	score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

	biz_info = models.ForeignKey(BusinessInfo, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	message = models.TextField(max_length=800)

	def __str__(self):
		return self.user.username
