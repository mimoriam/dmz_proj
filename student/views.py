from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import viewsets
# from .models import Subject, Student, SemesterConclusion, StudentModel from .serializers import StudentSerializer,
# SemesterSerializer, SemesterConclusionSerializer, StudentModelSerializer
from .models import StudentModel
from .serializers import StudentModelSerializer
from rest_framework import filters


class StudentList(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=registration_num', 'student_name', 'grade', 'subject__subject', 'subject__year__year', ]
    # lookup_field = 'registration_num'


class StudentDetail(generics.RetrieveAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class SemesterList(generics.ListCreateAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SemesterSerializer
#
#
# class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SemesterSerializer
#
#
# class SemesterConclusionList(generics.ListCreateAPIView):
#     queryset = SemesterConclusion.objects.all()
#     serializer_class = SemesterConclusionSerializer
#
#
# class SemesterConclusionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SemesterConclusion.objects.all()
#     serializer_class = SemesterConclusionSerializer
