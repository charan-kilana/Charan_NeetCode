from src.arrays.encode_decode_strings import Solution

sol = Solution()

def test_basic_strings():
    strs = ["neet", "code", "love"]
    encoded = sol.encode(strs)
    assert sol.decode(encoded) == strs

def test_single_string():
    strs = ["hello"]
    encoded = sol.encode(strs)
    assert sol.decode(encoded) == strs

def test_empty_list():
    strs = []
    encoded = sol.encode(strs)
    assert sol.decode(encoded) == strs

def test_empty_string():
    strs = [""]
    encoded = sol.encode(strs)
    assert sol.decode(encoded) == strs

def test_multiple_strings():
    strs = ["act", "cat", "dog"]
    encoded = sol.encode(strs)
    assert sol.decode(encoded) == strs