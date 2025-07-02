from rest_framework import serializers
from app.models import Motorista

class MotoristaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Motorista
        fields = ("id", "nome", "cor")