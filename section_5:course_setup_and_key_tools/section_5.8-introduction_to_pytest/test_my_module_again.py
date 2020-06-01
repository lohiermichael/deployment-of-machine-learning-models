import pytest

from my_module import square


@pytest.mark.parametrize(
    'inputs', [2, 3, 4.5]
    # The last test will fail
)
def test_square_return_value_is_int(inputs):
    # When
    subject = square(inputs)

    # Then
    assert isinstance(subject, int)
