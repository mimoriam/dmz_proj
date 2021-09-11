from django.contrib import admin

# from student.models import Student, Subject, SemesterConclusion, SemesterOrYear
from import_export.fields import Field
from student.models import StudentModel, YearModel, SubjectModel
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin


class StudentResource(resources.ModelResource):
    registration_num = Field(attribute='registration_num', column_name="Registration No.")
    student_name = Field(attribute='student_name', column_name="Student Name")
    total_num = Field(attribute='total_num', column_name="Total")
    grade = Field(attribute='grade', column_name="Grade")
    year = Field(attribute='year', column_name='Year', widget=ForeignKeyWidget(YearModel, 'year'))
    subject = Field(attribute='subject', column_name="Subject", widget=ForeignKeyWidget(SubjectModel, 'subject'))

    class Meta:
        model = StudentModel
        import_id_fields = ('registration_num',)
        skip_unchanged = True
        report_skipped = True
        fields = ('registration_num', 'student_name', 'total_num', 'grade', 'year', 'subject',)
        export_order = ('registration_num', 'student_name', 'total_num', 'grade', 'year', 'subject')

    def get_queryset(self):
        return self._meta.model.objects.order_by('registration_num')


class StudentAdmin(ImportExportModelAdmin):
    list_filter = ['registration_num']
    resource_class = StudentResource


admin.site.register(StudentModel, StudentAdmin)
admin.site.register(YearModel)
admin.site.register(SubjectModel)
# admin.site.register(Student)
# admin.site.register(SemesterOrYear)
# admin.site.register(Subject)
# admin.site.register(SemesterConclusion)
