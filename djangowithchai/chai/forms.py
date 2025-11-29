from django import forms
from .models import *


class ChaiVerityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), label="Select Chai Variety")