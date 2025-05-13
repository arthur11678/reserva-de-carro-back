from django.db.models import Q

from app.models import Reserva

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