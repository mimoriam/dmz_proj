from django.contrib import admin

from student.models import Student, Subject, SemesterConclusion, SemesterOrYear, StudentTestModel
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

admin.site.register(Student)
admin.site.register(SemesterOrYear)
admin.site.register(Subject)
admin.site.register(SemesterConclusion)


class StudentResource(resources.ModelResource):
    class Meta:
        model = StudentTestModel
        import_id_fields = ('registration_num',)
        skip_unchanged = False
        report_skipped = True
        fields = ('registration_num', 'student_name', 'total_num', 'grade', 'year',)
        export_order = ('registration_num', 'student_name', 'total_num', 'grade', 'year')

    def get_queryset(self):
        return self._meta.model.objects.order_by('registration_num')


class StudentAdmin(ImportExportModelAdmin):
    list_filter = ['registration_num']
    resource_class = StudentResource


admin.site.register(StudentTestModel, StudentAdmin)
