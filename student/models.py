from django.db import models


class Student(models.Model):
    session_choices = [
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021')
    ]

    program_choices = [
        ('BSc. Chemical Engineering', 'BSc. Chemical Engineering'),
        ('BSc. Computer Science', 'BSc. Computer Science')
    ]

    campus_choices = [
        ('Multan', 'Multan'),
        ('Lahore', 'Lahore')
    ]

    id = models.BigAutoField(primary_key=True)

    roll_number = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    cnic = models.IntegerField()
    date_of_birth = models.DateField()
    session = models.CharField(max_length=50, choices=session_choices)
    program = models.CharField(max_length=50, choices=program_choices)
    campus = models.CharField(max_length=50, choices=campus_choices)

    def __str__(self):
        return self.student_name


class Semester(models.Model):
    subject_grade_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('B', 'B')
    ]

    subject_name = models.CharField(max_length=50)
    subject_number = models.CharField(max_length=50)
    subject_sgpa = models.FloatField()
    subject_grade = models.CharField(max_length=50, choices=subject_grade_choices)
    subject_GPA = models.FloatField()
    subject_semester = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject_semester} Semester - {self.student} - {self.subject_name}'


class Semester_Conclusion(models.Model):
    semester_CH = models.FloatField()
    semester_cumulative = models.FloatField()
    total_gpa = models.FloatField()
    cgpa = models.FloatField()
    status = models.CharField(max_length=50)
    semester = models.OneToOneField(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.semester.subject_semester} Semester - {self.semester.student} - Result'
