from rest_framework import routers
from student.views.get_tutor_students import GetTutorStudents
from student.views.get_user_not_enrolled_couses import GetUserNotEnrolledCoursesViewSet

router = routers.DefaultRouter()
router.register(
    prefix=r'courses', viewset=GetUserNotEnrolledCoursesViewSet, basename="GetUserNotEnrolledCourses")
router.register(
    prefix=r'tutor/students', viewset=GetTutorStudents, basename="GetTutorStudents")
