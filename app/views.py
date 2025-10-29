from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.urls import reverse
import pdfkit, os
from django.templatetags.static import static
from django.conf import settings


WKHTMLTOPDF_PATH = os.getenv('WKHTMLTOPDF_PATH', r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)


##code pour déployer sur render il faut utiliser from_string et non from_url##
def generatePDF(request):
    # 1️⃣ On génère le HTML à partir du template
    html = render_to_string('index.html', {})

    # 2️⃣ Configuration wkhtmltopdf (pour Render/Linux)
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    # 3️⃣ Options PDF
    options = {
        'encoding': 'UTF-8',
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'margin-right': '0mm',
        'dpi': 300,
        'enable-local-file-access': None,
        'print-media-type': None,
        'no-background': False,
        'disable-smart-shrinking': None,
        'zoom': 1.0,
        # Éviter les coupures en plein texte
        'page-break-inside': 'avoid',
    }

    # 4️⃣ Génération du PDF directement depuis le HTML complet
    pdf = pdfkit.from_string(html, False, configuration=config, options=options)

    # 5️⃣ Envoi du PDF au navigateur
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv-hani-derrouiche.pdf"'
    return response


##code pour déployér sur autre que render (car render a du mal a support pdfkit##
#config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")#

#def generatePDF(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('home')), False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=test.pdf'

    return response##



def home(request):
    return render(request, 'index.html')

"""
Etape de traduction
1 Definir les variables a traduire
2 taper cette commande "python manage.py makemessages -l la_langue"
3 Donner leur equivalences dans la langue en question
4 compiler avec cette commande "python manage.py compilemessages
"""