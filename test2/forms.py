from django import forms
from test2.widget import nestedmultiselectfield

class Addressform(forms.ModelForm):
    class Meta:
        fields = ('properties_link')
        widgets = {'homepage':nestedmultiselectfield()}


