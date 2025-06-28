from django.contrib import admin
from .models import EmployeeModel
from .models import StudentModel
from .models import FacultyModel
admin.site.register(EmployeeModel)
admin.site.register(StudentModel)
admin.site.register(FacultyModel)