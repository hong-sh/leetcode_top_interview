"""
leetcode 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        dp = [0 for _ in range(len_prices)]
        min_val = prices[0]

        for i in range(1, len_prices):
            if i == 0:
                dp[i] = 0
                continue

            dp[i] = max(dp[i - 1], prices[i] - min_val)
            min_val = min(prices[i], min_val)

        return dp[len_prices - 1]
