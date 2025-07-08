from tabnanny import verbose
from django.db import models

from .Motorista import Motorista
from .Carro import Carro

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    data_inicio = models.DateTimeField(blank=False, null=False)
    data_fim = models.DateTimeField(blank=False, null=False)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + " - " +  self.motorista.nome + " - " + self.carro.nome
    
    class Meta:
        db_table = "reserva"
        managed = True
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-data_inicio"]