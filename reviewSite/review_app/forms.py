from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'album_score', 'cover_score', 'favorite_track', 'worst_track']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize crispy form helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Review'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Review'))