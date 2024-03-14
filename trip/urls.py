from django.urls import path

from trip.views import TripList, ShowTrip, AddTrip

urlpatterns = [
    path('', TripList.as_view(), name='home'),
    path('trip/<slug:slug>/', ShowTrip.as_view(), name='trip'),
    path('add/', AddTrip.as_view(), name='add'),

]

