from django.shortcuts import render

# Create your views here.

def Register(request):
    return render(request, 'formApp/registerform.html')