from src.stack.evaluate_reverse_polish_notation import Solution

sol = Solution()


def test_addition():
    assert sol.evalRPN(["2", "1", "+"]) == 3


def test_multiplication():
    assert sol.evalRPN(["2", "3", "*"]) == 6


def test_subtraction():
    assert sol.evalRPN(["5", "2", "-"]) == 3


def test_division():
    assert sol.evalRPN(["6", "2", "/"]) == 3


def test_complex_expression():
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9


def test_negative_division():
    assert sol.evalRPN(["-7", "2", "/"]) == -3


def test_large_expression():
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6