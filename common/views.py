from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import AdoptPetModel
from .forms import AdoptPetFormModel
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashListView(ListView):
    template_name = 'dashboard.html'


class HappyAdoptedPetsView(ListView):
    template_name = 'adopted_pets.html'
    model = AdoptPetModel


class HappyAdoptedPetsCreate(LoginRequiredMixin, CreateView):
    template_name = 'adopted_pets_create.html'
    form_class = AdoptPetFormModel
    success_url = reverse_lazy('happy_adopted')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
