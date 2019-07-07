from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from picklefield.fields import PickledObjectField
import json

class Person(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	# children = JSONField()

	def __str__(self):
		return self.name
	
	# def save(self, *args, **kwargs):
	# 	self.children = [{'id':self.name+'_Scheduled','title':'Scheduled'},
	# 					{'id':self.name+'_Actual','title':'Actual'}]
	# 	super(Person, self).save(*args, **kwargs) # Call the "real" save() method.
	
	# def get_children(self):
	# 	return [{'id':self.name+'_Scheduled','title':'Scheduled'},
	# 			{'id':self.name+'_Actual','title':'Actual'},]
	
	@property
	def children(self):
		return [{'id':self.name+'_Scheduled','title':'Scheduled'},
				{'id':self.name+'_Actual','title':'Actual'},]



class Event(models.Model):
	title = models.CharField(max_length = 100)
	start_scheduled = models.DateTimeField(auto_now_add = False) 
	end_scheduled = models.DateTimeField(auto_now_add = False) 
	start_actual = models.DateTimeField(auto_now_add = False) 
	end_actual = models.DateTimeField(auto_now_add = False)
	person = models.ForeignKey(Person, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.title