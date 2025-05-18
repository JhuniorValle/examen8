from django.db import models

class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    tipo_servicio = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='talleres/')

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, related_name='vehiculos')
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='vehiculos/')

    def __str__(self):
        return self.placa
