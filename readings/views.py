from django.shortcuts import render

# Create your views here.

def home(request):
    from readings.usccb import readings_context
    return render(request, 'readings/home.html', readings_context)
