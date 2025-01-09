"""
leetcode 169. Majority Element
https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # len_num = len(nums)
        counter = Counter(nums)
        max_count = 0
        max_num = 0
        for num, count in counter.items():
            if count > max_count:
                max_num = num
                max_count = count
        return max_num


sol = Solution()
print(sol.majorityElement(nums=[3, 2, 3]))
print(sol.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
