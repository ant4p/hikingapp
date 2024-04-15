from django.shortcuts import render
from django.views.generic import ListView

from tags.models import Tag
from trip.models import Trip


# Create your views here.

class ShowAllTags(ListView):
    template_name = 'tags/show_all_tags.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class TripTag(ListView):
    template_name = 'tags/show_tag.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return Trip.objects.filter(tag__slug=self.kwargs['slug'], published=True).select_related('category')
