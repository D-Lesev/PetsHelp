from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import AnimalAdoptReadyCreate
from .forms import AnimalAdoptReadyForm, AnimalAdoptForm

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


class AnimalAdoptFormSendView(LoginRequiredMixin, UpdateView):
    model = AnimalAdoptReadyCreate
    form_class = AnimalAdoptForm
    exclude = ['animal_name', 'animal_type', 'location', 'details', 'other', 'picture']
    template_name = 'animal_adopt_form.html'
    success_url = reverse_lazy('animal_success')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        for excluded_field in self.exclude:
            form.fields.pop(excluded_field)

        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet_model_fields = [field.name for field in AnimalAdoptReadyCreate._meta.get_fields()]

        field_values = {}
        for field in pet_model_fields:
            field_values[field] = self.object.__dict__.get(field)

        context['field_values'] = field_values

        return context


class AnimalAdoptSuccess(LoginRequiredMixin, TemplateView):
    template_name = "adopt_animal_success.html"

