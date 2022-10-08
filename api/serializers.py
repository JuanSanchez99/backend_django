from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'document_id', 'document_type', 'name', 'lastname', 'hobbies')
