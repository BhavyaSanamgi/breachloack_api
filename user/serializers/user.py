from rest_framework import serializers
from user.constants.enums import Gender, UserRole


class RegisterUserRequestValidationSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(required=True, choices=Gender.get_list_of_tuples())
    email = serializers.EmailField(required=True)
    phone_number = serializers.IntegerField(required=True)
    role = serializers.ChoiceField(required=True, choices=UserRole.get_list_of_tuples())
    bio = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        fields = "__all__"


class LoginUserRequestValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = "__all__"


class VerifyOTPRequestValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.IntegerField(required=True)

    class Meta:
        fields = "__all__"


class ResendOTPRequestValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = "__all__"
