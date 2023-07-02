from django.urls import path, include
from .views import HomePageView, DashListView, HappyAdoptedPetsView, HappyAdoptedPetsCreate


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashListView.as_view(), name='dashboard'),
    path('adopted-pets/', HappyAdoptedPetsView.as_view(), name='happy_adopted'),
    path('adopted-pets/create/', HappyAdoptedPetsCreate.as_view(), name='happy_adopted_create'),
]

