from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from slugify import slugify

from images.models import Image
from trip.forms import AddTripForm
# from trip.forms import AddTripForm
from trip.models import Trip
from trip.utils import generate_unique_slug


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
        return Trip.objects.filter(published=True).select_related('category')


class ShowTrip(DetailView):
    model = Trip
    template_name = 'trip/trip.html'
    context_object_name = 'trip'

    def get_success_url(self):
        return reverse('trip', kwargs={'slug': self.object.slug})


class AddTrip(CreateView):
    form_class = AddTripForm
    template_name = 'trip/add.html'

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_valid(self, form):

        """ Added 2 copy in DB. Problem in redefined method 'save' in model Trip?"""
        title = form.cleaned_data['title']
        print(form.cleaned_data['title'])
        date = form.cleaned_data['date']
        print(form.cleaned_data['date'])
        category = form.cleaned_data['category']
        print(form.cleaned_data['category'])
        title_photo = form.cleaned_data['title_photo']
        print(form.cleaned_data['title_photo'])
        content = form.cleaned_data['content']
        print(form.cleaned_data['content'])
        published = form.cleaned_data['published']
        print(form.cleaned_data['published'])
        slug = generate_unique_slug(Trip, title)
        print(slug)
        print('--------')


        # if not self.id:
        new_trip = Trip.objects.create(
            title=title,
            date=date,
            category=category,
            title_photo=title_photo,
            content=content,
            published=published,
            slug=slug,
        )
        print(new_trip)
        print(new_trip.title)
        print(new_trip.slug)
        new_trip.save()

        files = form.cleaned_data["image"]
        if files:
            print(form.cleaned_data['image'])
            for f in files:
                i = Image.objects.create(travel=new_trip, image=f)
                i.save()
                print(i)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('trip', kwargs={'slug': self.object.slug})


# class EditTrip(UpdateView):
#     model = Trip
#     # form_class = AddTripForm
#     template_name = 'trip/edit.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['slug'] = Trip.objects.all()
#         print(context)
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         """ through queryset? put slug field from copy object Trip from queryset? update this
#          trip object? create new images copy from cleaned_data files?"""
#         # instanse  = form.save(commit=False)
#         # instanse.slug = request.slug
#         title = form.cleaned_data['title']
#         date = form.cleaned_data['date']
#         category = form.cleaned_data['category']
#         title_photo = form.cleaned_data['title_photo']
#         content = form.cleaned_data['content']
#         published = form.cleaned_data['published']
#         update_model = Trip.objects.get(id=id(object))
#         update_trip = Trip.objects.update(
#             title=title,
#             date=date,
#             category=category,
#             title_photo=title_photo,
#             content=content,
#             published=published,
#         )
#         files = form.cleaned_data["image"]
#         for f in files:
#             Image.objects.create(image=f, travel=update_trip)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('trip', kwargs={'slug': self.object.slug})


class DeleteTrip(DeleteView):
    model = Trip
    template_name = 'trip/delete.html'
    success_url = reverse_lazy('home')
