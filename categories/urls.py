from django.urls import path

from categories.views import  show_category

urlpatterns = [

    path('category/<slug:slug>/', show_category, name='categories'),

]

