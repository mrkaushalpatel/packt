from django.shortcuts import render
from . import forms
# Create your views here.

def UserRegistrationView(request):
    form = forms.UserRegistrationForm
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print('form is Valid')
            print("First Name: ", form.cleaned_data['firstName'])
            print("Last Name: ", form.cleaned_data['lastName'])
            print("Email: ", form.cleaned_data['email'])
            print("Gender: ", form.cleaned_data['gender'])
    return render(request, 'formApp/userRegistration.html', {'form':form})
