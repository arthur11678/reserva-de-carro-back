from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from app.models import Carro
from app.serializers import CarroSerializer
from app.helpers import CarroHelper

class CarroView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        try:
            carro = Carro.objects.get(nome=request.data['nome'])
            return Response(status=400, data={"message": "Já existe um carro com esse nome"})
        except:
            carro = Carro.objects.create(nome=request.data['nome'])
            carro.save()
            return Response(CarroSerializer(carro, many=False).data)
    
    
    def list(self, request, *args, **kwargs):
        carros = Carro.objects.all()
        return Response(CarroSerializer(carros, many=True).data)

    @action(detail=False, methods=["GET"])
    def carros_livres(self, request, pk=None, *args, **kwargs):
       carros = CarroHelper.carros_livres(request.query_params)
       return Response(CarroSerializer(carros, many=True).data)
       