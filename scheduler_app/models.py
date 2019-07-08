from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from picklefield.fields import PickledObjectField
import json

class Person(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)
	# children = JSONField()

	def __str__(self):
		return self.title
	
	
	@property
	def children(self):
		return [{'id':self.title+'_Scheduled','title':'Scheduled'},
				{'id':self.title+'_Actual','title':'Actual'},]



class Event(models.Model):

	event_choices = [('Scheduled','Scheduled'),('Actual','Actual')]

	title = models.CharField(max_length = 100)
	start = models.DateTimeField(auto_now_add = False) 
	end = models.DateTimeField(auto_now_add = False)
	event_type = models.CharField(choices=event_choices, max_length=9) 
	person = models.ForeignKey(Person, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.title + '_' + self.event_type