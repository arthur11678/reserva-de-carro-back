import pytz
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from datetime import datetime

from app.helpers import ReservaHelper
from app.models import Reserva, Motorista, Carro
from app.serializers import ReservaSerializer

class ReservaView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data_inicio = datetime.strptime(request.data['data_inicio'], '%d/%m/%Y %H:%M').replace(tzinfo=pytz.timezone("America/Sao_Paulo"))
        data_fim = datetime.strptime(request.data['data_fim'], '%d/%m/%Y %H:%M').replace(tzinfo=pytz.timezone("America/Sao_Paulo"))
        carro = Carro.objects.get(id=request.data['carro'])
        motorista = Motorista.objects.get(id=request.data['motorista'])
        if ReservaHelper.existe_reserva(data_inicio, data_fim, carro, motorista):
            return Response(status=400, data={"message": "Já existe uma reserva para este carro ou motorista nesta data"})
        reserva = Reserva.objects.create(data_inicio=data_inicio, data_fim=data_fim, carro=carro, motorista=motorista)
        return Response(ReservaSerializer(reserva, many=False).data)