from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = [0] * len(strs)
        final = []

        for i in range(len(strs)):

            # Skip if already grouped
            if count[i]:
                continue
            
            group = [strs[i]]
            
            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    count[j] = 1
                    group.append(strs[j])
            
            final.append(group)

        return final