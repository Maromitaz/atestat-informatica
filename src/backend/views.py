from django.shortcuts import render
import re
from .models import Contact

def index(request):
    return render(request, 'index.html')
def showcar(request):
    return render(request, 'showcar.html')
def contact(request):
    if request.method == 'POST':
        numele_din_form = re.search(r"([$^]+[\s])",request.POST.get('numele'))
        prenume_din_form = re.search(r"([$^]+[\s])",request.POST.get('prenume'))
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        email_din_form = re.fullmatch(email_regex, request.POST.get('email'))
        mesajul_din_form = re.search(r"$^",request.POST.get('mesajul'))
        if numele_din_form:
            alert = {
            "alert":"""
                Trebuie sa va inserati numele!
            """,
            "display":"block"
            }
            return render(request, 'contact.html', alert)
        if prenume_din_form:
            alert ={ 
            "alert":"""
                Trebuie sa va inserati prenumele!
            """,
            "display":"block"
            }
            return render(request, 'contact.html', alert)
        if not email_din_form:
            alert ={ 
            "alert":"""
                Trebuie sa va inserati email-ul!
            """,
            "display":"block"
            }
            return render(request, 'contact.html', alert)
        if mesajul_din_form:
            alert = {
            "alert":"""
                Trebuie sa va inserati mesajul!
            """,
            "display":"block"
            }
            return render(request, 'contact.html', alert)
        numele = request.POST.get('numele')
        prenume = request.POST.get('prenume')
        email = request.POST.get('email')
        mesajul = request.POST.get('mesajul')
        contactData = Contact(numele=numele, prenumele=prenume, email=email, mesajul=mesajul)
        contactData.save()
    return render(request, 'contact.html',{"alert":"","display":"none"})
def mesaje(request):
    contactData = Contact.objects.all()
    context = {
        'mesaje': contactData
    }
    return render(request, 'mesaje.html', context)
def eroare_404(request, exception):
    return render(request, '404.html.', status=404)
    
