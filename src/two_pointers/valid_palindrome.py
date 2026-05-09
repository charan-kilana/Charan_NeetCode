class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Brute Force Method
        cleaned_string = ""

        # Remove non-alphanumeric characters
        # Convert uppercase to lowercase
        for ch in s:
            if ch.isalnum():
                cleaned_string += ch.lower()

        # Compare string with reverse
        return cleaned_string == cleaned_string[::-1]