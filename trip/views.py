from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from slugify import slugify

from images.models import Image
from trip.forms import AddTripForm
from trip.models import Trip
from trip.utils import generate_unique_slug, DataMixin


class AboutHikingapp(LoginRequiredMixin, TemplateView):
    template_name = 'trip/about.html'


class TripList(DataMixin, ListView):
    template_name = 'trip/index.html'
    context_object_name = 'trips'
    title_page = 'Main page'

    def get_queryset(self):
        return Trip.objects.filter(published=True).select_related('category')


class ShowTrip(DetailView):
    model = Trip
    template_name = 'trip/trip.html'
    context_object_name = 'trip'

    def get_success_url(self):
        return reverse('trip', kwargs={'slug': self.object.slug})


class AddTrip(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTripForm
    template_name = 'trip/add.html'


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        f = form.save()
        title = form.cleaned_data['title']
        f.slug = generate_unique_slug(Trip, title)
        images = form.cleaned_data['image']

        if images:
            for i in images:
                Image.objects.create(image=i, travel=f)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('trip', kwargs={'slug': self.object.slug})


class EditTrip(UpdateView):
    model = Trip
    template_name = 'trip/add.html'
    form_class = AddTripForm

    def form_valid(self, form):
        f = form.save()
        images = form.cleaned_data['image']

        if images:
            for i in images:
                Image.objects.create(image=i, travel=f)

        return super().form_valid(form)


class DeleteTrip(DeleteView):
    model = Trip
    template_name = 'trip/delete.html'
    success_url = reverse_lazy('home')
