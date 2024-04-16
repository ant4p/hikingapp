from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from tags.forms import AddTagForm
from tags.models import Tag
from trip.models import Trip
from trip.utils import generate_unique_slug


# Create your views here.

class ShowAllTags(ListView):
    template_name = 'tags/show_all_tags.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class TripTag(ListView):
    template_name = 'tags/show_tag.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return Trip.objects.filter(tag__slug=self.kwargs['slug'], published=True).select_related('category')


class AddTag(CreateView):
    form_class = AddTagForm
    template_name = 'tags/add_tag.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        f = form.save()
        tag = form.cleaned_data['tag']
        f.slug = generate_unique_slug(Tag, tag)

        return super().form_valid(form)

    success_url = reverse_lazy('all_tags')
