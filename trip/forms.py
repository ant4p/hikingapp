from django import forms

from trip.models import Trip


class AddTripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = [
            'title',
            'slug',
            'date',
            'title_photo',
            'content',
            'published',
            'category',
            'image',
        ]
        # widgets = {
        #     'photo': forms.ClearableFileInput(attrs={'allow_multiple_selected'})
        # }
