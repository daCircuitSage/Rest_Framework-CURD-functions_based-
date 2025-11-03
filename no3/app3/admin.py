from django.contrib import admin
from app3.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']
