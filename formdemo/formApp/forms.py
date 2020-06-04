from django import forms

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstName = forms.CharField(required=False)
    lastName = forms.CharField()
    email = forms.CharField()
    gender = forms.CharField(widget = forms.Select(choices=GENDER))
    password = forms.CharField(widget = forms.PasswordInput)
    ssn = forms.IntegerField()
