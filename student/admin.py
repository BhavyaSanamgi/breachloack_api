from django.contrib import admin
from .models import Tutor, Course, Student, Enrollment


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'tutor']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrollment_date']
