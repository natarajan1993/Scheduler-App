from rest_framework import serializers
from scheduler_app import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id','url','name','children')
        extra_kwargs = {
            'children':{
                'read_only':True
            }
        }