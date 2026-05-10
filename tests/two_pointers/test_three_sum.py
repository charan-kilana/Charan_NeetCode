from two_pointers.three_sum import Solution

sol = Solution()

def normalize(output):
    return sorted([sorted(triplet) for triplet in output])

def test_basic():
    result = sol.threeSum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert normalize(result) == normalize(expected)

def test_no_triplet():
    assert sol.threeSum([1, 2, 3]) == []

def test_all_zeroes():
    result = sol.threeSum([0, 0, 0, 0])
    expected = [[0, 0, 0]]
    assert normalize(result) == normalize(expected)

def test_empty_list():
    assert sol.threeSum([]) == []

def test_less_than_three():
    assert sol.threeSum([1, -1]) == []

def test_duplicate_triplets():
    result = sol.threeSum([-2, 0, 0, 2, 2])
    expected = [[-2, 0, 2]]
    assert normalize(result) == normalize(expected)