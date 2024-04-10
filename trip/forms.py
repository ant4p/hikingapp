import datetime

from django import forms

from images.forms import MultipleFileField
from images.models import Image
from trip.models import Trip


class AddTripForm(forms.ModelForm):

    image = MultipleFileField(required=False)
    slug = forms.CharField(required=False, widget=forms.HiddenInput())

    year = datetime.date.today().year
    date = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(year-5, year+3))))

    class Meta:
        model = Trip
        fields = [
            'title',

            'date',
            'title_photo',
            'content',
            'published',
            'category',

            # 'slug',
        ]
        # widgets = {'slug': forms.HiddenInput()}

    # AIFormSet = forms.inlineformset_factory(Trip, Image, fields='__all__')
