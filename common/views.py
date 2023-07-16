import PIL.ExifTags
from PIL import Image
from geopy.geocoders import Nominatim
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AdoptPetModel, AdoptionHomeModel, ShareAnimalModel
from .forms import AdoptPetFormModel, AdoptionHomeCreateModel, ShareAnimalForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class HelpAnimalsListView(ListView):
    template_name = 'help-animals.html'
    model = ShareAnimalModel


class HelpAnimalsCreateView(LoginRequiredMixin, CreateView):
    form_class = ShareAnimalForm
    template_name = 'help-animals-create.html'
    success_url = reverse_lazy('help_animals')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HelpAnimalsDetailView(LoginRequiredMixin, DetailView):
    model = ShareAnimalModel
    template_name = 'help-animals-details.html'

    def _get_location_by_fields(self):
        province = self.object.province
        city = self.object.city

        geoLoc = Nominatim(user_agent="GetLoc")
        coordinates = geoLoc.geocode(f'{province} {city}')

        return coordinates.latitude, coordinates.longitude

    def _get_gps_coordinates_photo(self, image):
        try:
            new_img = Image.open(image)

            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in new_img._getexif().items()
                if k in PIL.ExifTags.TAGS
            }

            north = exif['GPSInfo'][2]
            east = exif['GPSInfo'][4]

            lat = ((((north[0] * 60) + north[1]) * 60) + north[2]) / 60 / 60
            long = ((((east[0] * 60) + east[1]) * 60) + east[2]) / 60 / 60

            lat, long = float(lat), float(long)

            return lat, long
        except (KeyError, IOError, AttributeError):
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        image_path = self._get_gps_coordinates_photo(self.object.main_photo.path)

        if image_path is not None:
            context['latitude'] = image_path[0]
            context['longitude'] = image_path[1]
        else:
            location = self._get_location_by_fields()

            context['latitude'] = location[0]
            context['longitude'] = location[1]

        return context


class HappyAdoptedPetsView(ListView):
    template_name = 'adopted_pets.html'
    model = AdoptPetModel


class HappyAdoptedPetsCreate(LoginRequiredMixin, CreateView):
    template_name = 'adopted_pets_create.html'
    form_class = AdoptPetFormModel
    success_url = reverse_lazy('happy_adopted')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdoptionHomeCreate(LoginRequiredMixin, CreateView):
    template_name = 'adoption_home_create.html'
    form_class = AdoptionHomeCreateModel
    success_url = reverse_lazy('adoption_homes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdoptionHomeDetails(LoginRequiredMixin, DetailView):
    model = AdoptionHomeModel
    template_name = 'adoption_home_detail.html'


class AdoptionHomeView(LoginRequiredMixin, ListView):
    model = AdoptionHomeModel
    template_name = 'adoption_home.html'

