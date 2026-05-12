from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # Brute Force Method
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                value = prices[j] - prices[i]

                if value > profit:
                    profit = value

        return profit