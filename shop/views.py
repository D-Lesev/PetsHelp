from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import ItemShop
from .forms import ItemShopCreate
# Create your views here.


class PetShopView(ListView):
    model = ItemShop
    template_name = 'pet_shop.html'


class PetShopCreate(CreateView):  # TO add -> LoginRequiredMixin
    form_class = ItemShopCreate
    template_name = 'pet_shop_create.html'
    success_url = 'petshop'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetShopDetails(DetailView):   # TO add -> LoginRequiredMixin
    model = ItemShop
    template_name = 'pet_shop_detail.html'


class PetShopEdit(UpdateView):   # TO add -> LoginRequiredMixin, UserPassesTestMixin
    model = ItemShop
    template_name = 'pet_shop_edit.html'
    fields = ['title', 'price', 'available_quantity', 'description', 'location']

    # TODO: Add def test_func() for checking the current user


class PetShopDelete(DeleteView):  # TO add -> LoginRequiredMixin, UserPassesTestMixin
    model = ItemShop
    template_name = 'pet_shop_delete.html'
    success_url = 'petshop'  # Maybe reverse_lazy ???

    # TODO: Add def test_func() for checking the current user
