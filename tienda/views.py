from django.shortcuts import render

# Create your views here.

def tienda(request):
    return render(request,'tienda/templates/tienda/tienda.html')