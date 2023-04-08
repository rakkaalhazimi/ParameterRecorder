from app.auth import services


def test_email_validation_with_right_format():
    """
    GIVEN user enter his email
    WHEN user email format is correct
    THEN mark his email as valid
    """
    email = "test@test.com"
    is_valid = services.validate_email(email)
    assert is_valid


def test_email_validation_with_wrong_format():
    """
    GIVEN user enter his email
    WHEN user email format is incorrect
    THEN mark his email as invalid
    """
    email = "test#test.com"
    is_valid = services.validate_email(email)
    assert not is_valid
