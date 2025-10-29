from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.urls import reverse
import pdfkit, os

WKHTMLTOPDF_PATH = os.getenv('WKHTMLTOPDF_PATH', r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)



def generatePDF(request):
    # Rendre ton template HTML en texte
    html = render_to_string('index.html', {})  # tu peux passer un contexte ici

    # Configuration Linux pour Render
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    # Génération PDF à partir de la chaîne HTML
    pdf = pdfkit.from_string(html, False, configuration=config)

    # Réponse HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
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