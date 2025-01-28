from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Video', 'Video'),
        ('Document', 'Document'),
        ('MCQ Quiz', 'MCQ Quiz'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
//ManojKC123
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


# Intermediate table as student and course have many-to-many relationship
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
