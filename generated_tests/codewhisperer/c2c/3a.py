import pytest
from c2c import truncate_number

@pytest.mark.parametrize(
    "number, expected",
    [
        # Happy path tests
        (123.456, 0.456),  # normal float
        (0.999, 0.999),    # float less than 1
        (1.999, 0.999),    # float greater than 1
        (100.123, 0.123),  # large float
        (0.0, 0.0),        # zero

        # Edge cases
        (-123.456, -0.456),  # negative float
        (-0.999, -0.999),    # negative float less than 1
        (-1.999, -0.999),    # negative float greater than 1
        (1.0, 0.0),          # exactly 1
        (-1.0, 0.0),         # exactly -1
    ],
    ids=[
        "normal_float",
        "float_less_than_1",
        "float_greater_than_1",
        "large_float",
        "zero",
        "negative_float",
        "negative_float_less_than_1",
        "negative_float_greater_than_1",
        "exactly_1",
        "exactly_negative_1",
    ]
)
def test_truncate_number(number, expected):
    # Act
    result = truncate_number(number)

    # Assert
    assert result == expected
