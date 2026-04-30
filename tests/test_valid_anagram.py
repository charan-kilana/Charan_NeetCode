from arrays.valid_anagram import Solution

sol = Solution()

# -------- Basic --------
def test_valid_anagram_true():
    assert sol.isAnagram("anagram", "nagaram") == True

def test_valid_anagram_false():
    assert sol.isAnagram("rat", "car") == False

# -------- Edge Cases --------
def test_empty_strings():
    assert sol.isAnagram("", "") == True

def test_single_character():
    assert sol.isAnagram("a", "a") == True

def test_different_lengths():
    assert sol.isAnagram("a", "ab") == False

# -------- Case Sensitivity --------
def test_case_sensitive():
    assert sol.isAnagram("a", "A") == False

# -------- Repeated Characters --------
def test_repeated_characters():
    assert sol.isAnagram("aaab", "baaa") == True

def test_not_anagram_repeated():
    assert sol.isAnagram("aabb", "abbb") == False