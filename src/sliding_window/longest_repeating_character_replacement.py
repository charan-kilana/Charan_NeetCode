from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0

        # Brute Force Method
        for i in range(len(s)):

            count = defaultdict(int)

            for j in range(i, len(s)):
                count[s[j]] += 1

                substring_length = j - i + 1
                most_frequent_char_count = max(count.values())

                replacements_needed = substring_length - most_frequent_char_count

                if replacements_needed <= k:
                    max_length = max(max_length, substring_length)

        return max_length