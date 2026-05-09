from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # BFM
        nums_set = set(nums)
        output = 0

        for num in nums_set:

            length = 1

            # Start only from beginning of sequence
            if (num - 1) not in nums_set:

                while num + length in nums_set:
                    length += 1

            output = max(length, output)

        return output