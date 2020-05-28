from django.shortcuts import render

# Create your views here.

def template(request):
    myDict = {"name":"Kaushal Patel"}
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)


def employee(request):
    myDict = {"id":123,"name":"John","sal":10000}
    return render(request, 'templatesApp/employeeTemplate.html', myDict)
