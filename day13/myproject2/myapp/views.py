from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import EmployeeModel
from .models import StudentModel
from .models import FacultyModel  
from .forms import EmployeeForm


def insert_employee(request):
    context ={}
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_employee.html", context)  

def view_employee(request):
    ob=EmployeeModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_employee.html')
    return HttpResponse(temp.render(context,request))
from .forms import StudentForm
def insert_student(request):
    context ={}
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_student.html", context)  

def view_student(request):
    ob=StudentModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_student.html')
    return HttpResponse(temp.render(context,request))
def delete_employee(request,pk):
    EmployeeModel.objects.get(id=pk).delete()
    return render(request,
                  "delete_employee.html")
def delete_student(request,pk):
    EmployeeModel.objects.get(id=pk).delete()
    return render(request,
                  "delete_student.html")
from django.shortcuts import get_object_or_404, redirect
def update_employee(request,pk):
    obe = get_object_or_404(EmployeeModel, id=pk)
    if request.method == 'POST':
        obf = EmployeeForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_employee')#, id=pk
    else:
        formdata=EmployeeForm(instance=obe)
    return render(request, "update_employee.html", {'form':formdata})

def update_student(request,pk):
    obe = get_object_or_404(StudentModel, id=pk)
    if request.method == 'POST':
        obf = StudentForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_student')#, id=pk
    else:
        formdata=StudentModel(instance=obe)
    return render(request, "update_student.html", {'form':formdata})
def insert_faculty(request):
    context ={}
    ob_form = facultyForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_faculty.html", context)  

def view_faculty(request):
    ob=FacultyModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_faculty.html')
    return HttpResponse(temp.render(context,request))
