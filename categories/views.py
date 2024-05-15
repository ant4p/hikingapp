from django.views.generic import ListView

from categories.models import Category

from trip.models import Trip
from trip.utils import DataMixin


class ShowAllCategories(ListView):
    template_name = 'categories/show_all_categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class TripCategory(DataMixin, ListView):
    template_name = 'trip/index.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return (Trip.objects.filter(category__slug=self.kwargs['slug'], published=True).
                select_related('category').
                prefetch_related('user', 'tag'))
