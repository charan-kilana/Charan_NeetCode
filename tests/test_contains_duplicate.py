from arrays.contains_duplicate import Solution

sol = Solution()

# ---------------- Basic Cases ----------------
def test_duplicate_exists():
    assert sol.hasDuplicate([1, 2, 3, 1]) == True

def test_no_duplicate():
    assert sol.hasDuplicate([1, 2, 3, 4]) == False

# ---------------- Edge Cases ----------------
def test_empty_list():
    assert sol.hasDuplicate([]) == False

def test_single_element():
    assert sol.hasDuplicate([1]) == False

# ---------------- Multiple Duplicates ----------------
def test_multiple_duplicates():
    assert sol.hasDuplicate([1, 2, 2, 3, 3, 4]) == True

def test_all_same():
    assert sol.hasDuplicate([5, 5, 5, 5]) == True

# ---------------- Negative Numbers ----------------
def test_negative_numbers():
    assert sol.hasDuplicate([-1, -2, -3, -1]) == True

def test_negative_no_duplicate():
    assert sol.hasDuplicate([-1, -2, -3]) == False

# ---------------- Mixed Values ----------------
def test_mixed_numbers():
    assert sol.hasDuplicate([0, -1, 2, -1]) == True

def test_with_zero():
    assert sol.hasDuplicate([0, 1, 2, 3, 0]) == True

# ---------------- Large Input ----------------
def test_large_no_duplicate():
    nums = list(range(10000))
    assert sol.hasDuplicate(nums) == False

def test_large_with_duplicate():
    nums = list(range(10000)) + [9999]
    assert sol.hasDuplicate(nums) == True

# ---------------- Order Variation ----------------
def test_unsorted_with_duplicate():
    assert sol.hasDuplicate([4, 2, 1, 3, 2]) == True

def test_unsorted_no_duplicate():
    assert sol.hasDuplicate([4, 2, 1, 3]) == False
