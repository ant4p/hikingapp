from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from images.forms import AddImagesForm

from images.models import Image


class AddImages(FormView):
    form_class = AddImagesForm
    template_name = 'images/upload_image.html'
    success_url = reverse_lazy('home')
    # context_object_name = 'images'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]

        for f in files:
            Image(image=f).save()

        return super().form_valid(form)
