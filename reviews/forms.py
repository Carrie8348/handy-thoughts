from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """
    creates a form to add a new review for the product
    """
    class Meta:
        model = Reviews
        exclude = ('product', 'posted_by',) 