from rest_framework import viewsets
from user.serializers.user import ResendOTPRequestValidationSerializer


class ResendOTPView(viewsets.GenericViewSet):
    serializer_class = ResendOTPRequestValidationSerializer

    def create(self, request):
        from user.storages.storage_implementation import StorageImplementation
        from user.presenters.login_presenter_implementation import LoginPresenterImplementation
        from user.interactors.login_interactor import LoginInteractor

        request_data = request.data
        serializer = ResendOTPRequestValidationSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        email = request_data["email"]
        interactor = LoginInteractor(storage=StorageImplementation())
        response = interactor.login_user_wrapper(
            email=email, presenter=LoginPresenterImplementation())

        return response
