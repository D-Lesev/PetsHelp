from django.urls import path
from .views import AnimalAdoptCreateView, AnimalAdoptListView, AnimalAdoptFormSendView, AnimalAdoptSuccess

"""
10. http://127.0.0.1:8000/animals/share/ - share help for animal
    11. http://127.0.0.1:8000/animals/vetclinic/ - all animals in vet clinic
        http://127.0.0.1:8000/animals/vetclinic/create
    12. http://127.0.0.1:8000/animals/vetclinic/<str:slug>/ - details for animal in vet clinic | maybe <int:pk>/
    13. http://127.0.0.1:8000/animals/vetclinic/<str:slug>/edit/ - all animals in vet clinic | maybe <int:pk>/
    14. http://127.0.0.1:8000/animals/vetclinic/<str:slug>/delete/ - all animals in vet clinic | maybe <int:pk>/
"""


urlpatterns = [
    path('adoption/create/', AnimalAdoptCreateView.as_view(), name='animal_adopt_create'),
    path('adoption/', AnimalAdoptListView.as_view(), name='adoption_animals'),
    path('adoption/<int:pk>', AnimalAdoptFormSendView.as_view(), name='adopt_form'),
    path('adoption/success/', AnimalAdoptSuccess.as_view(), name='animal_success'),
]
