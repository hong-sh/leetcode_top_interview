"""
leetcode 45. Jump Game 2
https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List

INF = 10e15


class Solution:
    def jump(self, nums: List[int]) -> int:
        len_nums = len(nums)

        can_reach = [INF for _ in range(len_nums)]
        can_reach[-1] = 0

        for i in range(len_nums - 2, -1, -1):
            maximum_jump = nums[i]
            if i + maximum_jump >= len_nums - 1:
                can_reach[i] = 1
                continue

            for j in range(i + 1, i + maximum_jump + 1):
                if can_reach[j] < INF:
                    can_reach[i] = min(can_reach[i], can_reach[j] + 1)
                    continue

        return can_reach[0]


sol = Solution()
print(sol.jump(nums=[2, 3, 1, 1, 4]))
print(sol.jump(nums=[2, 3, 0, 1, 4]))
