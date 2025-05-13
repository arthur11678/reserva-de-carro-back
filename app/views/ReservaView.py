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
        return ReservaHelper.cria_reserva(request.data)

    def update(self, request, pk, *args, **kwargs):
        reserva = ReservaHelper.atualiza_reserva(pk, request.data)
        return Response(ReservaSerializer(reserva, many=False).data)