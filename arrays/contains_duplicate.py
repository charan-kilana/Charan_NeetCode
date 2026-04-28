from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # ---------------- Method 1: Set (Best) ----------------
        return len(set(nums)) < len(nums)


        # ---------------- Method 2: Sorting ----------------
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False


        # ---------------- Method 3: Dictionary ----------------
        # dict1 = {}
        # for num in nums:
        #     if num in dict1:
        #         return True
        #     dict1[num] = 1
        # return False
