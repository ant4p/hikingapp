from django import forms

from tags.models import Tag


class AddTagForm(forms.ModelForm):
    # tag = forms.CharField(max_length=40)

    class Meta:
        model = Tag
        fields = [
            'tag',
            # 'slug',
        ]
