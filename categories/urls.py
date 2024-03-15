from django.urls import path

from categories.views import CategoryList

urlpatterns = [

    path('category/<slug:slug>/', CategoryList.as_view(), name='categories'),

]

