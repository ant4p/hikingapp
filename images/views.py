from django.http import Http404
from django.shortcuts import get_list_or_404
from django.urls import reverse, reverse_lazy

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
            return reverse_lazy('empty_gallery')

            # raise Http404('Fall')


class ShowEmptyGallery(DetailView):
    template_name = 'images/empty_gallery.html'
