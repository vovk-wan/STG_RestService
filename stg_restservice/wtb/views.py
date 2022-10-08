from django.shortcuts import render
from django.views.generic import TemplateView


class Main(TemplateView):
    template_name = 'wtb/main.html'