from django.db import models

# Create your models here.

class Courses(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=50)

class Semesters(models.Model):
    semester_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=10)

class Offered_In(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE)
