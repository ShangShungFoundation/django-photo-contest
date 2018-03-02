from django import forms

from .models import Entry


class EntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        categories = initial['competition'].categories_list
        self.fields['category'] = forms.ChoiceField(
            choices=zip(categories, categories))
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['competition'].widget = forms.HiddenInput()

    class Meta:
        model = Entry
        exclude = ['metadata']
