from src.arrays.longest_consecutive_sequence import Solution

sol = Solution()

# -------- Basic --------
def test_basic():
    assert sol.longestConsecutive([100,4,200,1,3,2]) == 4

# -------- Consecutive sequence --------
def test_full_sequence():
    assert sol.longestConsecutive([1,2,3,4,5]) == 5

# -------- Empty array --------
def test_empty():
    assert sol.longestConsecutive([]) == 0

# -------- Single element --------
def test_single():
    assert sol.longestConsecutive([7]) == 1

# -------- Duplicates --------
def test_duplicates():
    assert sol.longestConsecutive([1,2,2,3]) == 3

# -------- Negative numbers --------
def test_negative_numbers():
    assert sol.longestConsecutive([-1,0,1,2]) == 4

# -------- No consecutive --------
def test_no_consecutive():
    assert sol.longestConsecutive([10,30,50]) == 1