from django import forms
from .models import Temple


class TempleForm(forms.ModelForm):

    class Meta:
        model = Temple
        temple_image = forms.ImageField(
            required=False,
            label='Image',
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control mb-2', 'placeholder':
                       'IMAGE', }
            ),
        )
        temple_icon = forms.ImageField(
            required=False,
            label='Image',
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control mb-2', 'placeholder':
                       'IMAGE', }
            ),
        )
        fields = [
            'temple_name',
            'temple_status',
            'temple_description',
            'temple_place',
            'temple_city',
            'temple_district',
            'temple_state',
            'temple_PINCode',
            'temple_image',
            'temple_icon',
            'temple_mail',
            'temple_phone',
            'temple_main_idol'
        ]
