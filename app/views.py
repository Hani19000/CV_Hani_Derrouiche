from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.urls import reverse
import pdfkit, os

WKHTMLTOPDF_PATH = os.getenv('WKHTMLTOPDF_PATH', r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)


##code pour déployer sur render il faut utiliser from_string et non from_url##
def generatePDF(request):
    # Préparer le contexte et charger le template HTML
    css_path = os.path.join(settings.STATIC_ROOT, 'css/style.css')  # chemin absolu en prod
    html = render_to_string('index.html', {})

    # Config wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    # Options wkhtmltopdf (marges, DPI, etc.)
    options = {
        'encoding': 'UTF-8',
        'page-size': 'A4',
        'margin-top': '10mm',
        'margin-bottom': '10mm',
        'margin-left': '10mm',
        'margin-right': '10mm',
        'dpi': 300,
        'enable-local-file-access': None,  # autorise wkhtmltopdf à lire les fichiers CSS
    }

    # Génération du PDF avec le CSS
    pdf = pdfkit.from_string(html, False, configuration=config, options=options, css=[css_path])

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