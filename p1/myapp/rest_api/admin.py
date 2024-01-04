from django.contrib import admin

# Register your models here.

from .models import MyModel, Student

class  MyAdmin(admin.ModelAdmin):
    list_display = ('tilte', 'description')


admin.site.register(MyModel)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'name', 'roll', 'address')

admin.site.register(Student)



 
