# Generated by Django 3.2.6 on 2021-09-02 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterOrYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('roll_number', models.CharField(max_length=50)),
                ('student_name', models.CharField(max_length=50)),
                ('cnic', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('session', models.CharField(choices=[('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], max_length=50)),
                ('program', models.CharField(choices=[('BSc. Chemical Engineering', 'BSc. Chemical Engineering'), ('BSc. Computer Science', 'BSc. Computer Science')], max_length=50)),
                ('campus', models.CharField(choices=[('Multan', 'Multan'), ('Lahore', 'Lahore')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentTestModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_number', models.CharField(max_length=50)),
                ('subject_sgpa', models.FloatField()),
                ('subject_grade', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('A', 'A'), ('B+', 'B+'), ('B-', 'B-'), ('B', 'B')], max_length=50)),
                ('subject_GPA', models.FloatField()),
                ('semester_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.semesteroryear')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterConclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_CH', models.FloatField()),
                ('semester_cumulative', models.FloatField()),
                ('total_gpa', models.FloatField()),
                ('cgpa', models.FloatField()),
                ('status', models.CharField(max_length=50)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.semesteroryear')),
            ],
        ),
    ]
