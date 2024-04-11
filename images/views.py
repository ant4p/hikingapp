from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
import random
from images.models import Image


class ShowGallery(ListView):
    template_name = 'images/gallery.html'
    context_object_name = 'images'

    def get_queryset(self):
        images = Image.objects.all()
        random_images = random.choices(images, k=9)
        return random_images



# class ShowEmptyGallery(DetailView):
#     template_name = 'images/empty_gallery.html'
