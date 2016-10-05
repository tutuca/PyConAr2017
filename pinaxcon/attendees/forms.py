# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

class BecasForm(forms.Form):
    nombre_completo = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    que_necesitas = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label=u"¿Qué necesitás?"
    )
    ingresa_el_texto = CaptchaField()

from .models import Attendee


class AttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee
        fields = [
            "full_name",
            "cv",
            "food_preference",
            "annotation",
            "show_to_sponsor",
        ]
