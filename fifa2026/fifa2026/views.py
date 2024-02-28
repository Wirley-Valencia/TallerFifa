from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm  
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def inicio(request):
    return render(request,'inicio.html',{
        #context
    })
    
@login_required(login_url='login')   
def index(request):
    return render(request,'index.html',{
        #context
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',
                  {

    })

def registro(request):
    
 
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        
        
        user = form.save()
        
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado con exito')
            return redirect('login')
         
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')



