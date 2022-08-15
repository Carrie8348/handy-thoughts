from django import forms
from .models import Free_Download


class FreeDownloadForm(forms.ModelForm):

    class Meta:
        model = Free_Download
        fields = '__all__'