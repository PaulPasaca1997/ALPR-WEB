from gzip import READ
from django.shortcuts import render, redirect
from torch import instance_norm
from django.contrib import auth
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from administracion.forms import UsuarioForm


def principal(request):
    return render(request, "principal.html")


def administracion(request):
    return render(request, "administracion.html")


def registroUsuario(request):

    if request.user.is_authenticated:
        return redirect('administracion')
    else:
        form = UsuarioForm()
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('administracion')

        context = {'form': form}
        return render(request, 'registro.html', context)


def loginPageA(request):
    if request.user.is_authenticated:
        return redirect('administracion')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('administracion')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'loginA.html', context)


def loginPageU(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('principal')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'loginU.html', context)


def logoutUser(request):
    logout(request)
    return redirect('principal')

# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------


##############################################################################
"""


# Create your views here.
def login1(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return redirect('login')
        else:
            return redirect('/')


def lista(request):
    context = {'lista': Usuario.objects.all()}
    return render(request, "lista.html", context)
    
    
def usuario(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UsuarioForm()
        else:
            usuario = Usuario.objects.get(pk=id)
            form = UsuarioForm(instance=usuario)
        return render(request, "registro.html", {'form': form})
    else:
        if id == 0:
            form = UsuarioForm(request.POST)
        else:
            usuario = Usuario.objects.get(pk=id)
            form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('/administrador/lista')


def eliminar(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('/administrador/lista')

##################################################################################################


def registroPlaca(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PlacaForm()
        else:
            placa = Placa.objects.get(pk=id)
            form = PlacaForm(instance=placa)
        return render(request, "placa/registro.html", {'form': form})
    else:
        if id == 0:
            form = PlacaForm(request.POST)
        else:
            placa = Placa.objects.get(pk=id)
            form = PlacaForm(request.POST, instance=placa)
        if form.is_valid():
            form.save()
        return redirect('/administrador/listaPlaca')


def listaPlaca(request):
    context = {'listaPlaca': Placa.objects.all()}
    return render(request, "placas/lista.html", context)
"""
