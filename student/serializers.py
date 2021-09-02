from rest_framework import serializers
from .models import Subject, Student, SemesterConclusion


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Subject


class SemesterConclusionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Subject
