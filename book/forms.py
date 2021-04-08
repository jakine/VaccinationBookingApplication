from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _




class ReservationForm(forms.Form):
    patient_name = forms.CharField(label='Name:', required=True)
    patient_surname = forms.CharField(label='Surname:', required=True)
    patient_phonenumber = forms.IntegerField(label='Phone Number:', required=True)
    patient_email = forms.EmailField(label='Email Address:', required=True)
    patient_checkDate = forms.DateField(label='Date:', required=True)
