from django.urls import path

from . import views

urlpatterns = [
    path('doctools/image2pdf', views.image2pdf, name='image2pdf'),
]