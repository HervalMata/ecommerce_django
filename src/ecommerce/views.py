from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

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
