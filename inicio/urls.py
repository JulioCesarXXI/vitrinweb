from  django.urls import path, include
from inicio import views


urlpatterns=[
    path('',views.inicio,name=''),
    #path('home/',views.inicio),
    path('blog/',include('blog.urls')),
    path('contacto/',include('contacto.urls')),
    path('servicios/',include('servicios.urls')),
    path('tienda/',include('tienda.urls')),
    path('about/',include('sobrenosotros.urls')),
]