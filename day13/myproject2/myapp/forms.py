from django.forms import fields  
from .models import EmployeeModel
from .models import StudentModel
from .models import FacultyModel  
from django import forms  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = EmployeeModel  
        fields = '__all__'  
class StudentForm(forms.ModelForm):  
    class Meta:    
      model = StudentModel 
      fields = '__all__'  
class FacultyForm(forms.ModelForm):  
    class Meta:    
      model = FacultyModel 
      fields = '__all__'  


