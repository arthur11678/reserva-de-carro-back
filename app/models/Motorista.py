from django.db import models

class Motorista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=24, unique=True, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = "motorista"
        managed = True
        verbose_name = "Motorista"
        verbose_name_plural = "Motoristas"
        ordering = ["-nome"]