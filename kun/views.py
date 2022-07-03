from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class Home(ListView):
    model = Article
    template_name = 'kun/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        regions = Region.objects.all()

        context['title'] = 'Kun.uz'
        context['cats'] = cats
        context['regions'] = regions
        return context