from src.two_pointers.valid_palindrome import Solution

sol = Solution()

# -------- Basic palindrome --------
def test_basic_palindrome():
    assert sol.isPalindrome("madam") == True

# -------- Mixed characters --------
def test_special_characters():
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True

# -------- Not palindrome --------
def test_not_palindrome():
    assert sol.isPalindrome("race a car") == False

# -------- Empty string --------
def test_empty_string():
    assert sol.isPalindrome("") == True

# -------- Numbers --------
def test_numbers():
    assert sol.isPalindrome("121") == True

# -------- Alphanumeric --------
def test_alphanumeric():
    assert sol.isPalindrome("0P") == False

# -------- Sentence palindrome --------
def test_sentence_palindrome():
    assert sol.isPalindrome("Was it a car or a cat I saw?") == True