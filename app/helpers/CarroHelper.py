from django.db.models import Q

from datetime import datetime

from app.models import Reserva, Carro

class CarroHelper:
    
    @classmethod
    def carros_livres(cls, params):
        data_inicio = datetime.fromtimestamp(int(params.get("data_inicio")))
        data_fim = datetime.fromtimestamp(int(params.get("data_fim")))
        carros_indisponiveis = Reserva.objects.filter(
            Q(data_inicio__lte=data_fim) & Q(data_fim__gte=data_inicio)
        ).values_list('carro_id', flat=True)
        
        # Buscar carros SEM reservas conflitantes
        carros_disponiveis = Carro.objects.exclude(id__in=carros_indisponiveis)
        return carros_disponiveis