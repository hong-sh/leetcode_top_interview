"""
leetcode 27. Remove Element
"""

from typing import List

INF = 1e9


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        k = len_nums
        for i in range(len_nums):
            if nums[i] == val:
                nums[i] = INF
                k -= 1

        return k


sol = Solution()
print(sol.removeElement(nums=[3, 2, 2, 3], val=3))
print(sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
