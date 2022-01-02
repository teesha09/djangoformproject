from django import forms
from . import views

class q1(forms.Form):
    Choice = forms.ChoiceField(label=var, choices=[('no','No'),('yes','Yes')])
