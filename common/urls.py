from django.urls import path, include
from .views import (HomePageView, HelpAnimalsListView, HappyAdoptedPetsView, HappyAdoptedPetsCreate,
                    AdoptionHomeCreate, AdoptionHomeView, HelpAnimalsCreateView, HelpAnimalsDetailView)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('help-animals/', HelpAnimalsListView.as_view(), name='help_animals'),
    path('help-animals/create/', HelpAnimalsCreateView.as_view(), name='help_animals_create'),
    path('help-animals/<int:pk>/detail/', HelpAnimalsDetailView.as_view(), name='help_animals_detail'),
    path('adopted-pets/', HappyAdoptedPetsView.as_view(), name='happy_adopted'),
    path('adopted-pets/create/', HappyAdoptedPetsCreate.as_view(), name='happy_adopted_create'),
    path('adopthomes/create/', AdoptionHomeCreate.as_view(), name='adoption_homes_create'),
    path('adopthomes/', AdoptionHomeView.as_view(), name='adoption_homes'),
]

