from django.contrib import admin

# Register your models here.
from student.models import Student, Semester, Semester_Conclusion

admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Semester_Conclusion)
