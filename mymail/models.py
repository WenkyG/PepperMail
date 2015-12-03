from django.db import models
from django.utils import timezone
import datetime

class user(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=40)
	user_id = models.CharField(max_length=20)
	gender = models.CharField(max_length = 10)
	password = models.CharField(max_length = 50)

class mailing(models.Model):
	sender = models.ForeignKey(user,related_name='send')
	receiver = models.ForeignKey(user,related_name='receive')
	subject = models.CharField(max_length = 100)
	messege = models.CharField(max_length = 1000)
	visited = models.BooleanField(default=False)

class sent_mai(models.Model):
	sende = models.ForeignKey(user,related_name='sendr')
	receive = models.ForeignKey(user,related_name='receiver')
	subject = models.CharField(max_length = 100)
	messege = models.CharField(max_length = 1000)

class trash(models.Model):
	m_id = models.IntegerField(default=0)
	sender = models.CharField(max_length = 20,default='mail')
	receiver = models.CharField(max_length = 20, default='mail')
	subject = models.CharField(max_length = 100,default='mail')
	messege = models.CharField(max_length = 1000,default='mail')