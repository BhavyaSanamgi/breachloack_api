from user.exceptions.custom_exceptions import \
    UserDoesNotExistsException, InvalidOTPException
from user.interactors.presenter_interface.verify_otp_presenter_intrface \
    import VerifyOTPPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface
from user.interactors.dtos import TokenDetailsDTO

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class VerifyOTPInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def verify_otp_wrapper(self, email: str, otp: int, presenter: VerifyOTPPresenterInterface):
        try:
            token_details = self.verify_otp(email=email, otp=otp)
        except UserDoesNotExistsException:
            return presenter.raise_user_does_not_exists_exception()
        except InvalidOTPException:
            return presenter.raise_invalid_otp_exception()
        return presenter.success_response(token_details=token_details)

    def verify_otp(self, email: str, otp: int):
        user_obj = self.storage.check_is_user_already_registered(
            email=email)
        if not user_obj:
            raise UserDoesNotExistsException

        self.storage.validate_otp(email=email, otp=otp)
        return self._get_token_details(user_obj=user_obj)

    def _get_token_details(self, user_obj) -> TokenDetailsDTO:
        from rest_framework_simplejwt.tokens import RefreshToken
        from datetime import timedelta
        from django.utils import timezone

        from user.interactors.dtos import TokenDetailsDTO
        refresh = RefreshToken.for_user(user_obj)
        refresh.access_token.set_exp(timezone.now() + timedelta(days=1))
        access_token = refresh.access_token
        access_token["role"] = user_obj.role
        token_details_dto = TokenDetailsDTO(
            access_token=str(access_token),
            refresh_token=str(refresh)
        )

        return token_details_dto


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role

        return token
