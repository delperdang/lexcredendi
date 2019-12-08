from django.shortcuts import render

# Create your views here.

def home(request):
    from litcal.usccb import litcal_context
    return render(request, 'litcal/home.html', litcal_context)
