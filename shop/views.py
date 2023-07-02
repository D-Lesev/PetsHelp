from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import ItemShop
from .forms import ItemShopCreate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class PetShopView(ListView):
    model = ItemShop
    template_name = 'pet_shop.html'


class PetShopCreate(LoginRequiredMixin, CreateView):
    form_class = ItemShopCreate
    template_name = 'pet_shop_create.html'
    success_url = reverse_lazy('petshop')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetShopDetails(LoginRequiredMixin, DetailView):
    model = ItemShop
    template_name = 'pet_shop_detail.html'


class PetShopEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ItemShop
    template_name = 'pet_shop_edit.html'
    fields = ['title', 'price', 'available_quantity', 'description', 'location']
    success_url = reverse_lazy('petshop')

    def test_func(self):
        item_shop = self.get_object()

        return self.request.user == item_shop.user


class PetShopDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ItemShop
    template_name = 'pet_shop_delete.html'
    success_url = reverse_lazy('petshop')

    def test_func(self):
        item_shop = self.get_object()

        return self.request.user == item_shop.user
