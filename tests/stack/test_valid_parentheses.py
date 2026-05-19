from src.stack.valid_parentheses import Solution

sol = Solution()


def test_valid_simple():
    assert sol.isValid("()") == True


def test_valid_multiple():
    assert sol.isValid("()[]{}") == True


def test_valid_nested():
    assert sol.isValid("([{}])") == True


def test_invalid_mismatch():
    assert sol.isValid("(]") == False


def test_invalid_wrong_order():
    assert sol.isValid("([)]") == False


def test_invalid_open_remaining():
    assert sol.isValid("(((") == False


def test_invalid_close_first():
    assert sol.isValid(")") == False


def test_empty_string():
    assert sol.isValid("") == True