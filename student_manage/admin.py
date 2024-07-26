from django.contrib import admin
from student_manage.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Student._meta.get_fields()]


admin.site.register(Student, StudentAdmin)
