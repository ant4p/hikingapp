from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from categories.models import Category
from trip.models import Trip


# Create your views here.
# class TripCategory(ListView):
#     # model = Trip
#     template_name = 'categories/show_category.html'
#     context_object_name = 'trips'
#
#     # allow_empty = False
#     def get_queryset(self):
#         return Trip.published.filter(cat__slug=self.kwargs['slug']).select_related('category')

def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Trip.published.filter(cat_id=category.pk).select_related('cat')
    return render(request, 'categories/show_category.html', )