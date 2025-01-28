from django import forms
from .models import Course, Student, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
