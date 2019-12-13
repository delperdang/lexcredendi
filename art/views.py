from django.shortcuts import render
from art.models import Record

# Create your views here.

def home(request):
    records = Record.objects.all().order_by('code')

    context = {
        'records': records
    }

    return render(request, 'art/home.html', context)