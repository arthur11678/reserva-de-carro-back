from tabnanny import verbose
from django.db import models

from .Motorista import Motorista
from .Carro import Carro

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    start_hour = models.TimeField(blank=False, null=False)
    end_hour = models.TimeField(blank=False, null=False)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "reserva"
        managed = True
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-start_date"]