from urllib import request

from django.http import Http404

from django.views.generic import ListView, DetailView
import random
from images.models import Image


class ShowGallery(ListView):
    template_name = 'images/gallery.html'
    context_object_name = 'images'

    def get_queryset(self):
        images = Image.objects.all()
        try:
            random_images = random.choices(images, k=9)
            return random_images
        except IndexError:
            pass
            # raise Http404()


# class ShowEmptyGallery(DetailView):
#     template_name = 'images/empty_gallery.html'
