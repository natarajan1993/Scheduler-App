from rest_framework import serializers
from scheduler_app import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id','url','title','children')
        extra_kwargs = {
            'children':{
                'read_only':True
            }
        }

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('id','url','title','start','end','person','event_type')
    
    def to_representation(self, instance):
        identifiers = dict()
        identifiers['id'] = instance.id
        identifiers['title'] = instance.title
        identifiers['start'] = instance.start
        identifiers['end'] = instance.end
        identifiers['resourceId'] = instance.person.title + '_' + instance.event_type 

        return identifiers