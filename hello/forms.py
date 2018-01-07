from django import forms


class MyForm(forms.Form):
    text = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            'type': 'search',
            'onfocus': "_i.classList.add('i_focus');",
            'onblur': "_i.classList.remove('i_focus');",
        }),
    )