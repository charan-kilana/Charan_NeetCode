class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Brute Force Method
        for i in range(len(s2)):
            sub_string = ""

            for j in range(i, len(s2)):
                sub_string = sub_string + s2[j]

            if sorted(sub_string[:len(s1)]) == sorted(s1):
                return True

        return False