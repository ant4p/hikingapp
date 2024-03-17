from django.urls import path

from categories.views import TripCategory

urlpatterns = [

    path('category/<slug:slug>/', TripCategory.as_view(), name='categories'),

]

