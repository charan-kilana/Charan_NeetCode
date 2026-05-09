from two_pointers.two_sum_ii import Solution

sol = Solution()

def test_basic():
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]

def test_middle_pair():
    assert sol.twoSum([1, 2, 3, 4, 8], 7) == [3, 4]

def test_last_pair():
    assert sol.twoSum([1, 2, 3, 4, 5], 9) == [4, 5]

def test_negative_numbers():
    assert sol.twoSum([-3, -1, 0, 2, 4], 1) == [1, 5]

def test_mixed_numbers():
    assert sol.twoSum([-2, 0, 3, 7], 5) == [1, 4]