from django.shortcuts import render

# Create your views here.

def template(request):
    myDict = {"name":"Kaushal Patel"}
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)
