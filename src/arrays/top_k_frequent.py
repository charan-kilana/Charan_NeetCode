from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # BFM
        seen = {}
        top_k = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        sorted_seen = list(dict(sorted(seen.items(), key=lambda x:x[1], reverse=True)).keys())

        for j in range(k):
            top_k.append(sorted_seen[j])
        
        return top_k
        