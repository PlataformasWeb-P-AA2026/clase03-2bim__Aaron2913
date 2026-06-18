from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    numero_provincias = models.IntegerField()
    numero_habitantes = models.IntegerField()

    def __str__(self):
        return "%s - Capital: %s" % (self.nombre, self.capital)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    # Aquí agregamos el campo pais fusionado
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='estudiantes', null=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre, self.apellido, self.cedula)

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)