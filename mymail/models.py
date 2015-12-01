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

	def __unicode__(self):
		return self.subject
