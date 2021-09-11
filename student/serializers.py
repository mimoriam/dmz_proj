from rest_framework import serializers
# from .models import Subject, Student, SemesterConclusion
from .models import StudentModel


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ['year']
        model = StudentModel
        depth = 2
        # lookup_field = 'registration_num'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'registration_num'}
        # }

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'
#         model = Student
#
#
# class SemesterSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'
#         model = Subject
#
#
# class SemesterConclusionSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'
#         model = Subject
