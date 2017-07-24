from django import forms
from django.core import validators


def check_for_z(value):
    if value[0] != 'z':
        raise forms.ValidationError("Needs to start with Z")

class FormName(forms.Form):
    name= forms.CharField(max_length=120, validators= [check_for_z])
    email= forms.EmailField()
    verify_email= forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher= forms.CharField(required=False, widget=forms.HiddenInput, validators= [validators.MaxLengthValidator(0)])
#VALIDATIONS FOR CHECKING EMAIL 
    def clean(self):
        all_clean_data= super().clean()
        email= all_clean_data['email']
        vemail= all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure emails match!")

    # def clean_botcatcher(self):
    #     botcatcher= self.cleaned_data['botcatcher']        EXAMPLE OF HOW TO VALIDATE DE HIDDEN INPUT
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BITCH!")
    #     return botcatcher
