from src.arrays.top_k_frequent import Solution

sol = Solution()

def normalize(output):
    return sorted(output)

# -------- Basic --------
def test_basic():
    result = sol.topKFrequent([1,1,1,2,2,3], 2)
    expected = [1, 2]
    assert normalize(result) == normalize(expected)

# -------- Single element --------
def test_single():
    assert sol.topKFrequent([1], 1) == [1]

# -------- Negative numbers --------
def test_negative():
    result = sol.topKFrequent([-1,-1,-2,-2,-2,3], 2)
    expected = [-2, -1]
    assert normalize(result) == normalize(expected)

# -------- k equals number of unique elements --------
def test_all_unique():
    result = sol.topKFrequent([1,2,3,4], 4)
    expected = [1,2,3,4]
    assert normalize(result) == normalize(expected)

# -------- duplicates --------
def test_duplicates():
    result = sol.topKFrequent([5,5,5,6,6,7], 1)
    expected = [5]
    assert result == expected

def test_same_elements():
    result = sol.topKFrequent([7, 7], 1)
    expected = [7]
    assert result == expected