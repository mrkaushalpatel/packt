from django.shortcuts import render, redirect
from fbvApp.models import Student
from fbvApp.forms import StudentForm

# Create your views here.
def getStudents(request):
    students = Student.objects.all()
    return render(request, 'fbvApp/index.html', {'students':students})

def createStudents(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'fbvApp/create.html', {'form':form})

def deleteStudents(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def updateStudents(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'fbvApp/update.html', {'student':student})
