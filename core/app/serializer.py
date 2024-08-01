# import serializer from rest_framework
from rest_framework import serializers
from .models import *

class SerializerName(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['firstname' , 'lastname'] #jinko json krna sirf inko field me add krega
        # exclude = ['id']#exclude krdega 
        field='__all__'

    # validator can be added here
    def validate(self,data):
        if data['firstname']=='x':
            raise serializers.ValidationError({'x':'y'})
        
        return data