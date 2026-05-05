from arrays.product_except_self import Solution

sol = Solution()

# Helper (order matters here, so direct compare)

def test_basic():
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_with_zero():
    assert sol.productExceptSelf([1, 2, 0, 4]) == [0, 0, 8, 0]

def test_all_zeros():
    assert sol.productExceptSelf([0, 0, 0]) == [0, 0, 0]

def test_single_element():
    assert sol.productExceptSelf([5]) == [1]

def test_negative_numbers():
    assert sol.productExceptSelf([-1, 1, -1, 1]) == [-1, 1, -1, 1]

def test_two_elements():
    assert sol.productExceptSelf([2, 3]) == [3, 2]