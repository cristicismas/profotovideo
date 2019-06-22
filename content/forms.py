from django import forms

class MultiplePhotosForm(forms.Form):
    photos = forms.CharField(
        max_length=50000,
        widget=forms.Textarea(),
        label='Photos'
    )