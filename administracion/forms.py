
from dataclasses import fields
from pyexpat import model
from tkinter import Label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from administracion.models import Placa


class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1','password2']

        labels = {
            'first_name': ' Nombres',
            'last_name': 'Apellidos',
            'username': ' Nombres',
            'first_name': ' Nombres',
            'last_name':' Nombres',
            'email':' Nombres', 
            'password1':' Nombres',
            'password2':' Nombres'
        }


class PlacaForm(forms.ModelForm):
    class Meta:
        model = Placa
        fields = ('placa', 'marca')
        labels = {
            'placa': ' Número de Placa',
            'marca': 'Marca Vehículo'
        }
