"""
leetcode 55. Jump Game
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        can_reach = [False for _ in range(len_nums)]
        can_reach[-1] = True

        for i in range(len_nums - 2, -1, -1):
            maximum_jump = nums[i]
            if i + maximum_jump >= len_nums - 1:
                can_reach[i] = True
                continue

            for j in range(i + 1, i + maximum_jump + 1):
                if can_reach[j] == True:
                    can_reach[i] = True
                    continue

        return can_reach[0]


sol = Solution()
# print(sol.canJump(nums=[2, 3, 1, 1, 4]))
# print(sol.canJump(nums=[3, 2, 1, 0, 4]))
print(sol.canJump(nums=[1, 2, 3]))
