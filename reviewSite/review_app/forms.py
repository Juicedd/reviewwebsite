from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AlbumReviewForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='Review')
    album_score = forms.IntegerField(label='Album Score', min_value=1, max_value=10)
    cover_score = forms.IntegerField(label='Cover Art Score', min_value=1, max_value=10)
    favorite_track = forms.CharField(label='Favorite Track', max_length=100)
    worst_track = forms.CharField(label='Least Favorite Track', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Review'))