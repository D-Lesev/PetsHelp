from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashListView(ListView):
    template_name = 'dashboard.html'


class HappyAdoptedPetsView(ListView):
    template_name = 'adopted_pets.html'
