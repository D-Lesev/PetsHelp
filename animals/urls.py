from django.urls import path, include
from .views import (AnimalAdoptCreateView, AnimalAdoptListView, AnimalAdoptFormSendView, AnimalAdoptSuccess,
                    VetClinicView, VetClinicCreate, VetClinicDetails, VetClinicEdit, VetClinicDelete)


urlpatterns = [
    path('adoption/create/', AnimalAdoptCreateView.as_view(), name='animal_adopt_create'),
    path('adoption/', AnimalAdoptListView.as_view(), name='adoption_animals'),
    path('adoption/<int:pk>', AnimalAdoptFormSendView.as_view(), name='adopt_form'),
    path('adoption/success/', AnimalAdoptSuccess.as_view(), name='animal_success'),
    path('vetclinic/', include([path('', VetClinicView.as_view(), name='vetclinic_view'),
                                path('create/', VetClinicCreate.as_view(), name='vetclinic_create'),
                                path('<int:pk>/', VetClinicDetails.as_view(), name='vetclinic_details'),
                                path('<int:pk>/edit/', VetClinicEdit.as_view(), name='vetclinic_edit'),
                                path('<int:pk>/delete/', VetClinicDelete.as_view(), name='vetclinic_delete')]))
]

