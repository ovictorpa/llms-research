import pytest
from c2c.4a import mean_absolute_deviation

@pytest.mark.parametrize(
    "numbers, expected, test_id",
    [
        # Happy path tests
        ([1, 2, 3, 4, 5], 1.2, "happy_path_1"),
        ([10, 20, 30, 40, 50], 12.0, "happy_path_2"),
        ([1.5, 2.5, 3.5, 4.5, 5.5], 1.2, "happy_path_3"),
        
        # Edge cases
        ([0, 0, 0, 0, 0], 0.0, "edge_case_all_zeros"),
        ([1], 0.0, "edge_case_single_element"),
        ([1, -1, 1, -1], 1.0, "edge_case_mixed_signs"),
        
        # Error cases
        ([], None, "error_case_empty_list"),
    ],
    ids=lambda param: param[2]
)
def test_mean_absolute_deviation(numbers, expected, test_id):
    
    # Act
    if numbers == []:
        with pytest.raises(ZeroDivisionError):
            mean_absolute_deviation(numbers)
    else:
        result = mean_absolute_deviation(numbers)
    
        # Assert
        assert result == pytest.approx(expected), f"Test {test_id} failed"