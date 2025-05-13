from django.db.models import Q
from rest_framework.response import Response

from datetime import datetime, timezone, tzinfo

from app.models import Reserva, Carro, Motorista
from app.serializers.Reserva import ReservaSerializer

class ReservaHelper:
    
    @classmethod
    def existe_reserva(cls, data_inicio, data_fim, carro, motorista):
        reservas = Reserva.objects.filter(
            Q(data_inicio__lte=data_fim) & Q(data_fim__gte=data_inicio) & (Q(carro=carro) | Q(motorista=motorista))
        )
        if reservas.exists():
            return True
        else:
            return False    
    
    @classmethod
    def cria_reserva(cls, data):
        data_inicio = datetime.strptime(data['data_inicio'], '%d/%m/%Y_%H:%M')
        data_fim = datetime.strptime(data['data_fim'], '%d/%m/%Y_%H:%M')
        carro = Carro.objects.get(id=data['carro'])
        motorista = Motorista.objects.get(id=data['motorista'])
        if cls.existe_reserva(data_inicio, data_fim, carro, motorista):
            return Response(status=400, data={"message": "Já existe uma reserva para este carro ou motorista nesta data"})
        reserva = Reserva.objects.create(data_inicio=data_inicio, data_fim=data_fim, carro=carro, motorista=motorista)
        return Response(ReservaSerializer(reserva, many=False).data)

    @classmethod
    def atualiza_reserva(cls, id, data):
        reserva = Reserva.objects.get(id=id)
        try:
            data_inicio = datetime.strptime(data['data_inicio'], '%d/%m/%Y_%H:%M')
            reserva.data_inicio = data_inicio
        except:
            pass
        
        try:
            data_fim = datetime.strptime(data['data_fim'], '%d/%m/%Y_%H:%M')
            reserva.data_fim = data_fim
        except:
            pass
        
        try:
            carro = Carro.objects.get(id=data['carro'])
            reserva.carro = carro
        except:
            pass
        
        try:
            motorista = Motorista.objects.get(id=data['motorista'])
            reserva.motorista = motorista
        except:
            pass
        
        reserva.save()