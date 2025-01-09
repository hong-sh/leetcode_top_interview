"""
Leetcode 80. Remove Duplicates from Sorted Array 2
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List
from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums_counter = Counter(nums)
        keys = sorted(list(nums_counter.keys()))
        k = 0
        idx = 0

        for num in keys:
            count = nums_counter[num]
            count = min(count, 2)
            k += count

            while idx < k:
                nums[idx] = num
                idx += 1

        nums = nums[:k]
        return k


sol = Solution()
print(sol.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
print(sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
