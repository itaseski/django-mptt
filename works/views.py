from django.shortcuts import render

from .models import Part


def show_parts(request):
    contex = {
        'parts': Part.objects.all()
        }
    return render(request, "works/parts.html", contex)
