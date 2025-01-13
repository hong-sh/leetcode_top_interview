"""
leetcode 122. Best Time to Buy and Sell Stock 2
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    total_income = 0

    def do_act(self, idx, prices, len_prices, buy_price, current_income):
        if idx == len_prices:
            self.total_income = max(self.total_income, current_income)
            return

        if buy_price == -1:  # not buy
            self.do_act(
                idx + 1, prices, len_prices, buy_price, current_income
            )  # not buy
            self.do_act(idx + 1, prices, len_prices, prices[idx], current_income)  # buy

        else:  # already buy
            if buy_price < prices[idx]:
                self.do_act(
                    idx + 1,
                    prices,
                    len_prices,
                    -1,
                    current_income + (prices[idx] - buy_price),
                )  # sell

            self.do_act(
                idx + 1, prices, len_prices, buy_price, current_income
            )  # not sell

    def maxProfit(self, prices: List[int]) -> int:
        self.total_income = 0
        self.do_act(0, prices, len(prices), -1, 0)
        return self.total_income



sol = Solution()
print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sol.maxProfit(prices=[1, 2, 3, 4, 5]))
print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))
