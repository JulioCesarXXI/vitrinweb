from django.urls import path
from sobrenosotros import views


urlpatterns=[
    path('',views.about,name='about')
]