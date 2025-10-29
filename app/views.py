from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from reportlab.pdfgen import canvas


def generatePDF(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, "Bonjour, ceci est un PDF généré avec ReportLab !")
    p.showPage()
    p.save()

    return response


def home(request):
    return render(request, 'index.html')

"""
Etape de traduction
1 Definir les variables a traduire
2 taper cette commande "python manage.py makemessages -l la_langue"
3 Donner leur equivalences dans la langue en question
4 compiler avec cette commande "python manage.py compilemessages
"""