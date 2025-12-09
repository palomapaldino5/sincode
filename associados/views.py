from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from associados.forms import AssociadosForm


# Página inicial de associados
def associados(request):
    return render(request, 'associados/index.html')


# CADASTRO COMPLETO
def cadastro(request):
    if request.method == "POST":
        form = AssociadosForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("usuario")
            email = form.cleaned_data.get("email")
            senha = form.cleaned_data.get("senha")

            # Criar usuário Django
            user = User.objects.create_user(
                username=usuario,
                email=email,
                password=senha
            )

            # Criar associado vinculado ao usuário
            associado = form.save(commit=False)
            associado.user = user
            associado.save()

            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("login")
    else:
        form = AssociadosForm()

    return render(request, "associados/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "logout realizado com sucesso!")
    return redirect("login")

# LOGIN
def login(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        user = authenticate(username=usuario, password=senha)

        if user is not None:
            django_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect("login")

    return render(request, "associados/login.html")
