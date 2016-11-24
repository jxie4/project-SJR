from django import forms
from .models import Input, Indicator, COUNTRIES, VARIABLES, YEARS

class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    country = forms.ChoiceField(choices=COUNTRIES, required=True,
                              widget=forms.Select(attrs = attrs)
                              )
    class Meta:

        model = Input
        fields = ['country']

class IndicatorForm(forms.ModelForm):

    # attrs = {'class ' : 'form-nav-control',
    #          'onchange ' : 'this.form.submit()'}

    variable = forms.ChoiceField(choices = VARIABLES, required = True,
                               widget = forms.Select())

    country = forms.MultipleChoiceField(choices=COUNTRIES, required=True,
                              widget=forms.SelectMultiple())
    class Meta:

        model = Indicator
        fields = ['country', 'variable']
