from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Brute Force Method
        timeTaken = []
        fleetNumber = 0

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            timeTaken.append([position[i], time])

        timeTaken.sort(reverse=True)

        slowestTime = 0

        for i in range(len(timeTaken)):
            if timeTaken[i][1] > slowestTime:
                slowestTime = timeTaken[i][1]
                fleetNumber += 1

        return fleetNumber