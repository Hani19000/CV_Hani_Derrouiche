from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.urls import reverse
import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")


def generatePDF(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('home')), False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=test.pdf'

    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

"""
Etape de traduction
1 Definir les variables a traduire
2 taper cette commande "python manage.py makemessages -l la_langue"
3 Donner leur equivalences dans la langue en question
4 compiler avec cette commande "python manage.py compilemessages
"""