from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-course/', views.create_course, name='create_course'),
    path('create-student/', views.create_student, name='create_student'),
    path('enroll-student/', views.enroll_student, name='enroll_student'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
