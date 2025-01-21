"""
leetcode 167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        summation = numbers[left] + numbers[right]
        while summation != target:
            if summation > target:
                right -= 1
            else:
                left += 1

            summation = numbers[left] + numbers[right]

        return [left + 1, right + 1]


sol = Solution()
print(sol.twoSum(numbers=[2, 7, 11, 15], target=9))
print(sol.twoSum(numbers=[2, 3, 4], target=6))
print(sol.twoSum(numbers=[-1, 0], target=-1))
