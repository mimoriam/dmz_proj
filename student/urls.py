from django.contrib import admin
from django.urls import path

# from student.views import StudentDetail, StudentList, SemesterDetail, SemesterList, SemesterConclusionList, \
#     SemesterConclusionDetail
from student.views import StudentTestList, StudentTestDetail

urlpatterns = [
    path('', StudentTestList.as_view()),
    # path('<int:pk>/', StudentDetail.as_view()),
    # path('', StudentList.as_view()),
    # path('semester/<int:pk>/', SemesterDetail.as_view()),
    # path('semester/', SemesterList.as_view()),
    # path('semester_conc/<int:pk>/', SemesterConclusionDetail.as_view()),
    # path('semester_conc/', SemesterConclusionList.as_view()),
]
