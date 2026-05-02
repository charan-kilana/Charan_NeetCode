from arrays.group_anagrams import Solution

sol = Solution()

def normalize(output):
    return sorted([sorted(group) for group in output])

# -------- Basic --------
def test_group_anagrams_basic():
    result = sol.groupAnagrams(["act","pots","tops","cat","stop","hat"])
    expected = [["hat"],["act","cat"],["stop","pots","tops"]]
    assert normalize(result) == normalize(expected)

# -------- Single word --------
def test_single():
    assert sol.groupAnagrams(["abc"]) == [["abc"]]

# -------- Empty --------
def test_empty():
    assert sol.groupAnagrams([]) == []

# -------- No anagrams --------
def test_no_anagrams():
    result = sol.groupAnagrams(["a","b","c"])
    expected = [["a"],["b"],["c"]]
    assert normalize(result) == normalize(expected)

# -------- All same --------
def test_all_same():
    result = sol.groupAnagrams(["aaa","aaa","aaa"])
    expected = [["aaa","aaa","aaa"]]
    assert normalize(result) == normalize(expected)