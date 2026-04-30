class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BFM
        if (len(nums)>=2 and len(nums)<=1000):
            for i in range(0,len(nums)):
                for j in range(i+1,len(nums)):
                    if(nums[i]+nums[j])==target:
                        return [i, j]
