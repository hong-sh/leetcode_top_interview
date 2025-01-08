"""
leetcode 88.Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_nums2 = len(nums2)
        nums3 = []
        left, right = 0, 0
        while left < m and right < len_nums2:
            if nums1[left] <= nums2[right]:
                nums3.append(nums1[left])
                left += 1

            else:
                nums3.append(nums2[right])
                right += 1

        while left < m:
            nums3.append(nums1[left])
            left += 1

        while right < len_nums2:
            nums3.append(nums2[right])
            right += 1

        for i, v in enumerate(nums3):
            nums1[i] = v


sol = Solution()
print(sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(sol.merge(nums1=[1], m=1, nums2=[], n=0))
print(sol.merge(nums1=[0], m=0, nums2=[1], n=1))
