from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

class Contacto(generic.TemplateView):
    template_name = 'localizacion/contacto.html'

