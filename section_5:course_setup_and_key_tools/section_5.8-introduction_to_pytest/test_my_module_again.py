from my_module import square


def test_square_return_value_is_int(input_value):
    # When
    subject = square(input_value)

    # Then
    assert isinstance(subject, int)
