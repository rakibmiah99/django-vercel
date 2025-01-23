from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'John Doe',
        'date': date.today(),
    }

    return render(request, 'index.html', context)
