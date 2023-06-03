from rest_framework import serializers
from student.models import Course
from django.contrib.auth import get_user_model


User = get_user_model()


class GetStudentCoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class GetUserDetails(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
