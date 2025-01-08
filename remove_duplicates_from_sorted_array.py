"""
leetcode 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        remove_nums = list(set(nums))
        remove_nums.sort()

        for i, v in enumerate(remove_nums):
            nums[i] = v

        k = len(remove_nums)
        nums = nums[:k]

        return k


sol = Solution()
print(sol.removeDuplicates(nums=[1, 1, 2]))
print(sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
