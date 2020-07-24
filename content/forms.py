from django import forms

class MultiplePhotosForm(forms.Form):
    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='Photos'
    )