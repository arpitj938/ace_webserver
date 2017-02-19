from __future__ import unicode_literals

from django.db import models

class login_data(models.Model):
	login_id=models.SmallIntegerField(primary_key=True)
	group_id=models.SmallIntegerField(default=0)
	password=models.CharField(max_length=120,blank=True,null=True)
	otp= models.CharField(max_length=10,blank=True,null=True)
	email=models.CharField(max_length=200,blank=True,null=True)
	email_flag=models.BooleanField(default=False)
	content_flag=models.BooleanField(default=False)

# Create your models here.
