import pytest
from c2c.8a import sum_product

@pytest.mark.parametrize(
    "numbers, expected_sum, expected_product",
    [
        # Happy path tests
        ([1, 2, 3, 4], 10, 24),  # sum: 1+2+3+4=10, product: 1*2*3*4=24
        ([0, 1, 2, 3], 6, 0),    # sum: 0+1+2+3=6, product: 0*1*2*3=0
        ([5, 5, 5, 5], 20, 625), # sum: 5+5+5+5=20, product: 5*5*5*5=625

        # Edge cases
        ([], 0, 1),              # sum: 0, product: 1 (empty list)
        ([0], 0, 0),             # sum: 0, product: 0 (single zero)
        ([1], 1, 1),             # sum: 1, product: 1 (single one)
        ([-1, -2, -3], -6, -6),  # sum: -1-2-3=-6, product: -1*-2*-3=-6

        # Error cases
        ([1, 2, 'a'], None, None), # invalid input: string in list
    ],
    ids=[
        "sum_1_2_3_4",
        "sum_0_1_2_3",
        "sum_5_5_5_5",
        "empty_list",
        "single_zero",
        "single_one",
        "negative_numbers",
        "invalid_input_string"
    ]
)
def test_sum_product(numbers, expected_sum, expected_product):

    # Act
    try:
        result = sum_product(numbers)
    except TypeError:
        result = (None, None)

    # Assert
    assert result == (expected_sum, expected_product)
