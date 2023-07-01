from django.urls import path, include
from .views import HomePageView, DashListView, HappyAdoptedPetsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashListView.as_view(), name='dashboard'),
    path('adopted-pets/', HappyAdoptedPetsView.as_view(), name='happy_adopted'),
]

