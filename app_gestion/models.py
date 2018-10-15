from django.db import models


# Create your models here.
class Cliente(models.Model):
    SEXO = (
        ('H', 'Hombre'),
        ('M', 'Mujer')
    )

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='avatar/', blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    precio_total = models.FloatField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
