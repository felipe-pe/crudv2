from django import forms

class CodigoForm(forms.Form):
    code = forms.CharField(label='Código de voo', max_length=10)