from django.contrib import admin
from .models import Greeting, Faculty, StudentFaculty


# Register your models here.
admin.site.register(Greeting)
admin.site.register(Faculty)
admin.site.register(StudentFaculty)