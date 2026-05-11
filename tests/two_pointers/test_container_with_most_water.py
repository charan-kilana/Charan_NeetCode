from two_pointers.container_with_most_water import Solution

sol = Solution()

def test_basic():
    assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_small_case():
    assert sol.maxArea([1,1]) == 1

def test_same_heights():
    assert sol.maxArea([2,2,2]) == 4

def test_increasing():
    assert sol.maxArea([1,2,3,4,5]) == 6

def test_decreasing():
    assert sol.maxArea([5,4,3,2,1]) == 6

def test_large_walls():
    assert sol.maxArea([4,3,2,1,4]) == 16