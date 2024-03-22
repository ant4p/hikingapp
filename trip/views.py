from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView

from trip.forms import AddTripForm
# from trip.forms import AddTripForm
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
        return Trip.objects.filter(published=True).select_related('category')


class ShowTrip(DetailView):
    model = Trip
    template_name = 'trip/trip.html'
    context_object_name = 'trip'

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Trip.published, slug=self.kwargs[self.slug_url_kwarg])


class AddTrip(CreateView):
    form_class = AddTripForm
    # model = Trip
    # fields = '__all__'
    template_name = 'trip/add.html'

    # context_object_name = 'trip'
    #
    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_valid(self, form):
    #     files = form.cleaned_data["photo"]
    #     for f in files:
    #         f = Trip.objects.create(photo='photo')
    #     return super().form_valid()

    # def form_valid(self, form):
    #     form.save(commit=False)
    #     for photo in self.request.FILES.getlist('photo'):
    #         Trip.objects.create(photo=photo)
    #     return super().form_valid(form)
    # def post(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         photos = request.FILES.getlist('photo')
    #
    #         for f in photos:
    #             info = Trip(photo=f)
    #             info.save()
    #     return render(request, 'trip', kwargs={'slug': self.object.slug})

    def get_success_url(self):
        return reverse('trip', kwargs={'slug': self.object.slug})


class EditTrip(UpdateView):
    model = Trip
    fields = '__all__'
    template_name = 'trip/add.html'

    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('trip', kwargs={'slug': self.object.slug})


class DeleteTrip(DeleteView):
    model = Trip
    template_name = 'trip/delete.html'
    success_url = reverse_lazy('home')
