from django.shortcuts import render
# from art.models import Record

# Create your views here.

def home(request):
    # records = Record.objects.all().order_by('code')

    return render(request, 'art/home.html')

def details(request, album):
    # records = Record.objects.filter(album=album)

    context = {
        # 'records': records
    }

    return render(request, 'art/details.html', context)