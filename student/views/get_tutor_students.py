from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response
from student.serializers.courses import GetUserDetails
from student.models import Enrollment, Course
from django.contrib.auth import get_user_model

User = get_user_model()


class GetTutorStudents(viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserDetails

    def list(self, request):
        login_user = self.request.user
        tutor_course_ids = list(Course.objects.filter(
            tutor_id=login_user.id).values_list("id", flat=True))
        user_ids = list(Enrollment.objects.filter(
            course_id__in=tutor_course_ids).values_list("student__user_id", flat=True))
        students = User.objects.filter(id__in=user_ids)
        serializer = GetUserDetails(students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
