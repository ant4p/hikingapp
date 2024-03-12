from django.shortcuts import render
from django.views.generic import ListView

from trip.models import Trip


# # Create your views here.
# class ShowTrips(ListView):
#     template_name = 'base.html'
#
#     def get_queryset(self):
#         return

# def get_page(request):
#     return render(request, 'trip/index.html')


class TripList(ListView):
    template_name = 'trip/index.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return Trip.objects.all()
