import os
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ItemShop
from .forms import ItemShopCreate


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

    def get_success_url(self):
        item_pk = self.object.pk

        return reverse('details_petshop', kwargs={'pk': item_pk})

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

    def form_valid(self, form):
        self.object = self.get_object()

        picture_path = os.path.join(settings.MEDIA_ROOT, self.object.main_photo.name)

        if os.path.exists(picture_path):
            os.remove(picture_path)

        self.object.delete()

        return HttpResponseRedirect(self.success_url)
