from typing import List

class Solution:
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.bruteForceMethod(temperatures)
        # later use:
        # return self.stackMethod(temperatures)

    def stackMethod(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        # Later optimized method
        return res

    def bruteForceMethod(self, temperatures: List[int]) -> List[int]:
        out_day = []

        for i in range(len(temperatures)):
            count = 0
            found = False

            for j in range(i + 1, len(temperatures)):
                count += 1

                if temperatures[j] > temperatures[i]:
                    out_day.append(count)
                    found = True
                    break

            if not found:
                out_day.append(0)

        return out_day