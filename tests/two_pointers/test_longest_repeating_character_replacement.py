from sliding_window.longest_repeating_character_replacement import Solution

sol = Solution()

def test_basic():
    assert sol.characterReplacement("AAABABB", 1) == 5

def test_example_two():
    assert sol.characterReplacement("AABBBABBA", 1) == 6

def test_all_same():
    assert sol.characterReplacement("AAAA", 2) == 4

def test_k_zero():
    assert sol.characterReplacement("AABABBA", 0) == 2

def test_replace_two():
    assert sol.characterReplacement("ABAB", 2) == 4

def test_single_character():
    assert sol.characterReplacement("A", 1) == 1

def test_no_replacement_needed():
    assert sol.characterReplacement("BBBBB", 0) == 5