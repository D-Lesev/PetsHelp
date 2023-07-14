from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return self.request.GET.get('next')
