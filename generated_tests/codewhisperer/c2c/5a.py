import pytest
from c2c.5a import intersperse

@pytest.mark.parametrize(
    "numbers, delimiter, expected",
    [
        # Happy path tests
        ([1, 2, 3], 0, [1, 0, 2, 0, 3]),  # normal case
        ([4, 5], 9, [4, 9, 5]),  # two elements
        ([7], 3, [7]),  # single element

        # Edge cases
        ([], 1, []),  # empty list
        ([1, 2, 3, 4, 5], -1, [1, -1, 2, -1, 3, -1, 4, -1, 5]),  # negative delimiter
        ([0, 0, 0], 0, [0, 0, 0, 0, 0]),  # all zeros

        # Error cases
        ([1, 2, 3], None, [1, None, 2, None, 3]),  # None as delimiter
        ([1, 2, 3], "a", [1, "a", 2, "a", 3]),  # string as delimiter
    ],
    ids=[
        "normal_case",
        "two_elements",
        "single_element",
        "empty_list",
        "negative_delimiter",
        "all_zeros",
        "none_as_delimiter",
        "string_as_delimiter",
    ]
)
def test_intersperse(numbers, delimiter, expected):

    # Act
    result = intersperse(numbers, delimiter)

    # Assert
    assert result == expected
