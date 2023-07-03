from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AnimalAdoptReadyCreate
from .forms import AnimalAdoptReadyForm

# Create your views here.


class AnimalAdoptCreateView(LoginRequiredMixin, CreateView):
    form_class = AnimalAdoptReadyForm
    template_name = 'animal_adopt_create.html'
    success_url = reverse_lazy('adoption_animals')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnimalAdoptListView(LoginRequiredMixin, ListView):
    model = AnimalAdoptReadyCreate
    template_name = 'animals_adopted_ready.html'

