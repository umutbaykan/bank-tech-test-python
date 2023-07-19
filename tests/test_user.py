from lib.user import User


def test_user_instance_creation():
    """
    Creates a user class instance with no default account
    """
    user = User()
    assert user.account == None
