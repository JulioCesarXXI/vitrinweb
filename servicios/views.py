from django.shortcuts import render

# Create your views here.

def servicios(request):
    return render(request,'servicios/templates/servicios/servicios.html')