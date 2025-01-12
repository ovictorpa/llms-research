import pytest
from c2c.6a import parse_nested_parens

@pytest.mark.parametrize(
    "paren_string, expected, test_id",
    [
        # Happy path tests
        ("()", [1], "single_pair"),
        ("(())", [2], "nested_pair"),
        ("() ()", [1, 1], "two_pairs"),
        ("((())) (()) ()", [3, 2, 1], "mixed_depths"),
        
        # Edge cases
        ("", [], "empty_string"),
        (" ", [], "single_space"),
        ("() (()) ((()))", [1, 2, 3], "increasing_depths"),
        ("((())) (()) () ()", [3, 2, 1, 1], "mixed_depths_with_extra"),
        
        # Error cases
        ("(()", [2], "unbalanced_open"),
        (")(", [0], "unbalanced_close"),
        ("() )(", [1, 0], "balanced_and_unbalanced"),
    ],
    ids=lambda x: x[2]
)
def test_parse_nested_parens(paren_string, expected, test_id):
    # Act
    result = parse_nested_parens(paren_string)

    # Assert
    assert result == expected, f"Test {test_id} failed: expected {expected}, got {result}"
