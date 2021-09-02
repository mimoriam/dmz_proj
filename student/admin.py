from django.contrib import admin

# Register your models here.
from import_export.forms import ExportForm

from student.models import Student, Subject, SemesterConclusion, SemesterOrYear, StudentTestModel
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Student)
admin.site.register(SemesterOrYear)
admin.site.register(Subject)
admin.site.register(SemesterConclusion)


class StudentResource(resources.ModelResource):
    class Meta:
        model = StudentTestModel

    def __init__(self, form_fields=None):
        super().__init__()
        self.form_fields = form_fields

    def get_export_fields(self):
        return [self.fields[f] for f in self.form_fields]


class BookExportForm(ExportForm):
    pass


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('student_name',)
    list_filter = ['id']
    resource_class = StudentResource

    def get_export_resource_kwargs(self, request, *args, **kwargs):
        formats = self.get_export_formats()
        form = BookExportForm(formats, request.POST or None)
        # get list of fields from form (hard-coded to 'author' for example purposes)
        form_fields = ("student_name",)
        return {"form_fields": form_fields}


admin.site.register(StudentTestModel, StudentAdmin)
