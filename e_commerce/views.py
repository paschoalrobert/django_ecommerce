from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
import requests
def home_page(request):
    context = {
        "title": "Pagina principal",
        "content": "Bem-Vindo a página principal"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Pagina sobre",
        "content": "Bem-Vindo a página sobre"
    }
    return render(request, "about/view.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Pagina de Contato",
        "content": "Bem-Vindo a pagina de contato",
        "form": contact_form

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)
