import pytest
from c2c.2a import separate_paren_groups

@pytest.mark.parametrize(
    "paren_string, expected_result",
    [
        # Happy path tests
        ("(())", ["(())"], id="nested_parentheses"),
        ("()()", ["()", "()"], id="two_separate_groups"),
        ("((()))(())", ["((()))", "(())"], id="complex_nested_and_separate"),
        
        # Edge cases
        ("", [], id="empty_string"),
        ("()", ["()"], id="single_pair"),
        ("(((())))", ["(((())))"], id="deeply_nested"),
        ("()()()()", ["()", "()", "()", "()"], id="multiple_separate_pairs"),
        
        # Error cases
        ("(()", [], id="unbalanced_open"),
        (")(", [], id="unbalanced_close"),
        ("(()))", [], id="unbalanced_extra_close"),
    ]
)
def test_separate_paren_groups(paren_string, expected_result):
    # Act
    result = separate_paren_groups(paren_string)

    # Assert
    assert result == expected_result