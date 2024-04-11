from django.views.generic import ListView
import random
from images.models import Image


class ShowGallery(ListView):
    template_name = 'images/gallery.html'
    context_object_name = 'images'

    def get_queryset(self):
        images = Image.objects.all()
        random_images = random.choices(images, k=9)
        return random_images

