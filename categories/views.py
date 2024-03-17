from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from categories.models import Category
from trip.models import Trip


class TripCategory(ListView):
    # model = Trip
    template_name = 'categories/show_category.html'
    context_object_name = 'trips'
    # allow_empty = False

    def get_queryset(self):
        return Trip.objects.filter(category__slug=self.kwargs['slug'], published=True)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category = context['trips'][0].category
    #     context['title'] = 'Category - ' + category.title
    #     context['category_selected'] = category.pk
    #     return context
    #     # return self.get_mixin_context(context, title='Category - ' + category.title, category_selected=category.pk, )

# def show_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     trips = Trip.objects.filter(category_id=category.pk)
#     data = {
#         'title': f'CateGGGory: {category.title}',
#         'trips': trips,
#         'category_selected': category.pk,
#     }
#     return render(request, 'categories/show_category.html', data)

