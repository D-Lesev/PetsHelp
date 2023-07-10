from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import AnimalAdoptReadyCreate, AnimalAtVetClinic
from .forms import AnimalAdoptReadyForm, AnimalAdoptForm, AnimalVetClinicCreateForm


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


class VetClinicView(LoginRequiredMixin, ListView):
    model = AnimalAtVetClinic
    template_name = 'vetclinic.html'


class VetClinicCreate(LoginRequiredMixin, CreateView):
    model = AnimalAtVetClinic
    form_class = AnimalVetClinicCreateForm
    template_name = 'vetclinic_create.html'
    success_url = reverse_lazy('vetclinic_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VetClinicDetails(LoginRequiredMixin, DetailView):
    model = AnimalAtVetClinic
    template_name = 'vetclinic_details.html'


class VetClinicEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AnimalAtVetClinic
    form_class = AnimalVetClinicCreateForm
    template_name = 'vetclinic_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('vetclinic_details', kwargs={'pk': pk})

    def test_func(self):
        vetclinic_animal = self.get_object()

        return vetclinic_animal.user == self.request.user


class VetClinicDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AnimalAtVetClinic
    template_name = 'vetclinic_delete.html'
    success_url = reverse_lazy('vetclinic_view')

    def test_func(self):
        vet_object = self.get_object()

        return self.request.user == vet_object.user
