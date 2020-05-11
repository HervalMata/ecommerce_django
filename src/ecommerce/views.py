from django.http import HttpResponse
from django.shortcuts import render


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
    context = {
        "title": "Contato",
        "content": "Deixe-nos entrar em contato"
    }
    return render(request, "home_page.html", context)
