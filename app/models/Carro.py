from django.db import models

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=24, unique=True, null=False)
    
    def __str__(self):
        return self.nome
    
  
    class Meta:
        db_table = 'carro'
        managed = True
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ["-nome"]