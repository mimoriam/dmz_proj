from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Subject, Student, SemesterConclusion, StudentTestModel
from .serializers import StudentSerializer, SemesterSerializer, SemesterConclusionSerializer, StudentTestModelSerializer
from rest_framework import filters


class StudentTestList(generics.ListCreateAPIView):
    queryset = StudentTestModel.objects.all()
    serializer_class = StudentTestModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['registration_num']


class StudentTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentTestModel.objects.all()
    serializer_class = StudentTestModelSerializer

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
