from django import forms

from images.forms import MultipleFileField
from trip.models import Trip


class AddTripForm(forms.ModelForm):

    image = MultipleFileField(required=False)

    class Meta:
        model = Trip
        fields = [
            'title',

            'date',
            'title_photo',
            'content',
            'published',
            'category',
        ]
