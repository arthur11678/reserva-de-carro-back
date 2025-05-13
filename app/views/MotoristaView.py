from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from app.models import Motorista
from app.serializers import MotoristaSerializer

class MotoristaView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        try:
            motorista = Motorista.objects.get(nome=request.data['nome'])
            return Response(status=400, data={"message": "Já existe um motorista com esse nome"})
        except:
            motorista = Motorista.objects.create(nome=request.data['nome'])
            motorista.save()
            return Response(MotoristaSerializer(motorista, many=False).data)
    
    def list(self, request, *args, **kwargs):
        motoristas = Motorista.objects.all()
        return Response(MotoristaSerializer(motoristas, many=True).data)
    