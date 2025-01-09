"""
leetcode 189. Rotate Array
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        sliced_idx = k if k < len_nums else k % len_nums
        sliced_idx = len_nums - sliced_idx

        new_nums = nums[sliced_idx:] + nums[:sliced_idx]
        for i in range(len_nums):
            nums[i] = new_nums[i]


sol = Solution()
print(sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
print(sol.rotate(nums=[-1, -100, 3, 99], k=2))
