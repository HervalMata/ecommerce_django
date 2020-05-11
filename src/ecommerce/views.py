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
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
