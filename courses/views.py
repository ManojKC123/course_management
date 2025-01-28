from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Course, Student, Enrollment
from .forms import CourseForm, StudentForm, EnrollmentForm


def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})


def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            password = User.objects.make_random_password()
            user = User.objects.create_user(username=student.email, email=student.email, password=password)
            student.user = user
            student.save()

            send_mail(
                'Your Student Account',
                f'Hello {student.name}, your account has been created. Your login email is {student.email} and password is {password}.',
                'admin@example.com',
                [student.email],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'courses/create_student.html', {'form': form})


def enroll_student(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll_student.html', {'form': form})


def admin_dashboard(request):
    enrollments = Enrollment.objects.select_related('student', 'course')
    return render(request, 'courses/admin_dashboard.html', {'enrollments': enrollments})
