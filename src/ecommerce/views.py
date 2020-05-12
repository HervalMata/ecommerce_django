from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title": "Hello World!",
        "content": "Bemvindo ao site"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Sobre",
        "content": "Tudo sobre o site"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contato",
        "content": "Deixe-nos entrar em contato",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("Usuário logado")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Erro")
    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})
