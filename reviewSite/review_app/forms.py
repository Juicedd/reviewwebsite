from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Review, Track

class ReviewForm(forms.ModelForm):
    favorite_track = forms.ModelChoiceField(queryset=Track.objects.none(), required=False)
    worst_track = forms.ModelChoiceField(queryset=Track.objects.none(), required=False)
    album_score = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)], required=True)
    cover_score = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)], required=True)

    class Meta:
        model = Review
        fields = ['content', 'album_score', 'cover_score', 'favorite_track', 'worst_track']

    def __init__(self, *args, **kwargs):
        album = kwargs.pop('album', None)
        super().__init__(*args, **kwargs)
        if album:
            tracklist = Track.objects.filter(album=album)
            self.fields['favorite_track'].queryset = tracklist
            self.fields['worst_track'].queryset = tracklist
        # Initialize crispy form helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Review'))