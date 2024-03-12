from django.shortcuts import render
from django.views.generic import ListView


# # Create your views here.
# class ShowTrips(ListView):
#     template_name = 'base.html'
#
#     def get_queryset(self):
#         return

def get_page(request):
    return render(request, 'trip/index.html')
