from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import CustomUserCreationForm
from django.views import View

# Create your views here.
@login_required()
def home(request):
    return render(request, 'home.html')

@login_required
def clients(request):
    return render(request, 'clients.html')

def exit(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect('home')  # Redirige a una página después de registrarse
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def payments(request):
    return render(request, 'payments.html')

def citas(request):
    return render(request, 'citas.html')