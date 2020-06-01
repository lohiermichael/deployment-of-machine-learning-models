from my_module import square


def test_square_return_value_is_int():
    # When
    subject = square(3)

    # Then
    assert isinstance(subject, int)
