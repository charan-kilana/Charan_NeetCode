from src.arrays.two_sum import Solution

sol = Solution()

# -------- Basic --------
def test_two_sum_basic():
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_second_pair():
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]

# -------- Edge Cases --------
def test_two_sum_negative_numbers():
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_zero():
    assert sol.twoSum([0, 4, 3, 0], 0) == [0, 3]

def test_two_sum_large():
    nums = list(range(1000))
    nums.append(999)
    assert sol.twoSum(nums, 1998) == [999, 1000]

# -------- Duplicate values --------
def test_two_sum_duplicates():
    assert sol.twoSum([3, 3], 6) == [0, 1]

def test_two_sum_same_values():
    assert sol.twoSum([5, 5], 10) == [0, 1]