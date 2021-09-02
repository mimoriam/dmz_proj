from django.contrib import admin

# Register your models here.
from student.models import Student, Subject, SemesterConclusion, SemesterOrYear

admin.site.register(Student)
admin.site.register(SemesterOrYear)
admin.site.register(Subject)
admin.site.register(SemesterConclusion)
