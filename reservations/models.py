from django.db import models


class Client(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Department(models.Model):
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField(blank=True) 
    capacidad = models.PositiveIntegerField(default=1)  
    disponibilidad = models.BooleanField(default=True)  

    def __str__(self):
        return self.nombre

class Reservation(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True, blank=True)  
    fecha_fin = models.DateField(null=True, blank=True) 
    propiedad = models.ForeignKey(Department, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.cliente.nombre} - {self.propiedad.nombre} desde {self.fecha_inicio} hasta {self.fecha_fin}"
