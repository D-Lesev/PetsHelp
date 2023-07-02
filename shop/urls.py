from django.urls import path
from .views import PetShopView, PetShopCreate, PetShopEdit, PetShopDetails, PetShopDelete


urlpatterns = [
    path('', PetShopView.as_view(), name='petshop'),
    path('create/', PetShopCreate.as_view(), name='create_petshop'),
    path('<int:pk>/', PetShopDetails.as_view(), name='details_petshop'),
    path('<int:pk>/edit/', PetShopEdit.as_view(), name='edit_petshop'),
    path('<int:pk>/delete/', PetShopDelete.as_view(), name='delete_petshop'),
]

