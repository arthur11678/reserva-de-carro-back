from rest_framework import serializers
from app.models import Reserva
from app.serializers import MotoristaSerializer, CarroSerializer

class ReservaSerializer(serializers.ModelSerializer):
    
    carro = CarroSerializer(many=False)
    motorista = MotoristaSerializer(many=False)
    
    class Meta:
        model = Reserva
        fields = ("id", "data_inicio", "data_fim", "hora_inicio", "hora_fim", "carro", "motorista")