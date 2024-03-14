from django.urls import path

from trip.views import TripList, ShowTrip, AddTrip

urlpatterns = [
    path('', TripList.as_view(), name='home'),
    path('add/', AddTrip.as_view(), name='add'),

    path('trip/<slug:slug>/', ShowTrip.as_view(), name='trip'),


]

