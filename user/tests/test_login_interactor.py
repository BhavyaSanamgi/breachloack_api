from unittest.mock import create_autospec

from user.interactors.login_interactor import LoginInteractor
from user.interactors.presenter_interface.login_presenter_interface \
    import LoginPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface


def test_login_user_wrapper_raises_user_does_not_exist_exception():
    # Arrange
    email = "test@example.com"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(LoginPresenterInterface)
    interactor = LoginInteractor(storage=storage)

    storage.get_user_phone_number.return_value = '345345345343'
    storage.check_is_user_already_registered.return_value = None

    # Act
    interactor.login_user_wrapper(email=email, presenter=presenter)

    # Assert
    presenter.raise_user_does_not_exists_exception.assert_called_once()
