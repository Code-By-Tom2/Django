from django import forms # type: ignore
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'description']
