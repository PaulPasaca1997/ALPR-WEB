from pickle import NONE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Rol (models.Model):
    roles=models.CharField(max_length=25)
    
    #PARA MOSTRAR LOS NOMBRES EN LA TABLA, SINO SE PONE SE MUESTRAN COMO OBJETOS
    def __str__(self):
        return self.roles
    
    
class Usuario(models.Model):
    username= None
    cedula = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=100)
    contrasenarep = models.CharField(max_length=100)

    
class Placa(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=7)   
    
 # https://www.youtube.com/watch?v=N6jzspc2kds&ab_channel=CodAffection 
 #https://bootsnipp.com/tags/login