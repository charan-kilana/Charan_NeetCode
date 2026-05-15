from sliding_window.permutation_in_string import Solution

sol = Solution()

def test_basic_true():
    assert sol.checkInclusion("ab", "eidbaooo") == True

def test_basic_false():
    assert sol.checkInclusion("ab", "eidboaoo") == False

def test_same_string():
    assert sol.checkInclusion("abc", "abc") == True

def test_single_character_true():
    assert sol.checkInclusion("a", "a") == True

def test_single_character_false():
    assert sol.checkInclusion("a", "b") == False

def test_permutation_middle():
    assert sol.checkInclusion("adc", "dcda") == True

def test_empty_s2():
    assert sol.checkInclusion("abc", "") == False