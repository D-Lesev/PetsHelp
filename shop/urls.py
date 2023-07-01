from django.urls import path
from .views import PetShopView


urlpatterns = [
    path('', PetShopView.as_view(), name='petshop'),
    path('create/', PetShopView.as_view(), name='create_petshop'),
    path('<int:pk>/', PetShopView.as_view(), name='details_petshop'),
    path('<int:pk>/edit/', PetShopView.as_view(), name='edit_petshop'),
    path('<int:pk>/delete/', PetShopView.as_view(), name='delete_petshop'),
]

