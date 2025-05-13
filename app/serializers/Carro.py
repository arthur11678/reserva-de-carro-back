from rest_framework import serializers
from app.models import Carro

class CarroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Carro
        fields = ("id", "nome")