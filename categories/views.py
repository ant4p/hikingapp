from django.shortcuts import render
from django.views.generic import ListView

from categories.models import Category
from trip.models import Trip


# Create your views here.
class CategoryList(ListView):
    model = Category
    template_name = 'categories/show_category.html'
    context_object_name = 'trips'

    # def get_queryset(self):
    #     return Trip.published.filter(cat__slug=self.kwargs['slug'].select_related('category'))
