from django.contrib import admin
from .models import Employees

# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):

    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(Employees,EmployeesAdmin)
