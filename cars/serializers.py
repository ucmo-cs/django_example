from rest_framework import serializers
from cars.models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'make', 'model', 'year']
