from django.urls import path, include
from .views import (HomePageView, DashListView, HappyAdoptedPetsView, HappyAdoptedPetsCreate,
                    AdoptionHomeCreate, AdoptionHomeView)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashListView.as_view(), name='dashboard'),
    path('adopted-pets/', HappyAdoptedPetsView.as_view(), name='happy_adopted'),
    path('adopted-pets/create/', HappyAdoptedPetsCreate.as_view(), name='happy_adopted_create'),
    path('adopthomes/create/', AdoptionHomeCreate.as_view(), name='adoption_homes_create'),
    path('adopthomes/', AdoptionHomeView.as_view(), name='adoption_homes'),
]

