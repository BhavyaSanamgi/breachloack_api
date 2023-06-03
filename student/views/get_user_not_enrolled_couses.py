from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response
from student.serializers.courses import GetStudentCoursesSerializer
from student.models import Student, Course, Enrollment


class GetUserNotEnrolledCoursesViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = GetStudentCoursesSerializer

    def list(self, request):
        login_user = self.request.user
        try:
            student = Student.objects.get(user_id=login_user.id)
            enrolled_course_ids = list(student.courses.all().values_list("id", flat=True))
            not_enrolled_courses = Course.objects.exclude(id__in=enrolled_course_ids)
        except Student.DoesNotExist:
            not_enrolled_courses = Course.objects.all()

        serializer = GetStudentCoursesSerializer(not_enrolled_courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        import datetime
        request_data = self.request.data

        user_id = request_data["user_id"]
        course_ids = request_data["course_ids"]

        student = Student.objects.get(user_id=user_id)

        enrollment_objs = [
            Enrollment(student=student, course_id=course_id, enrollment_date=datetime.datetime.now())
            for course_id in course_ids
        ]
        Enrollment.objects.bulk_create(enrollment_objs)
        return Response("Success", status=status.HTTP_200_OK)
