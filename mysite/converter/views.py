from django.shortcuts import render
from django.http.response import HttpResponse

from .models import *


def index(request):
    requests = ConvertRequest.objects.all()
    contex = {
        'requests': requests,
        'title': 'Список запросов'
    }
    return render(request, 'converter/index.html', contex)
