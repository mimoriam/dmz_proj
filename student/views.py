from rest_framework import generics
from .models import Semester, Student, SemesterConclusion
from .serializers import StudentSerializer, SemesterSerializer, SemesterConclusionSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SemesterList(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterConclusionList(generics.ListCreateAPIView):
    queryset = SemesterConclusion.objects.all()
    serializer_class = SemesterConclusionSerializer


class SemesterConclusionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SemesterConclusion.objects.all()
    serializer_class = SemesterConclusionSerializer
