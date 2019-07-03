from django.db import models
from django.contrib.auth.models import User



class Person(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name



class Event(models.Model):
	title = models.CharField(max_length = 100)
	start_scheduled = models.DateTimeField(auto_now_add = False) 
	end_scheduled = models.DateTimeField(auto_now_add = False) 
	start_actual = models.DateTimeField(auto_now_add = False) 
	end_actual = models.DateTimeField(auto_now_add = False)
	person = models.ForeignKey(Person, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.title