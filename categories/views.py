from django.views.generic import ListView


from trip.models import Trip


class TripCategory(ListView):
    template_name = 'categories/show_category.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return Trip.objects.filter(category__slug=self.kwargs['slug'], published=True).select_related('category')


