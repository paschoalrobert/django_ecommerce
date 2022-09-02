from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context

def home_page(request):
    context = {
        "title": "Pagina principal"
        "content": "Bem-Vindo a página principal"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "Pagina sobre"
        "content": "Bem-Vindo a página sobre"
    }
    return render(request, "about_page.html", context)


def contact_page(request):
    context = {
        "title": "Pagina de Contato"
        "content": "Bem-Vindo a pagina de contato"
    }
    return render(request, "contact_page.html", context)
