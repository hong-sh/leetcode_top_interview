"""
leetcode 274. H-Index 
https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        len_citations = len(citations)

        for i in range(len_citations, 0, -1):
            if citations[(len_citations - i)] >= i:
                return i

        return 0


sol = Solution()
print(sol.hIndex(citations=[3, 0, 6, 1, 5]))
print(sol.hIndex(citations=[1, 3, 1]))
print(sol.hIndex(citations=[1, 2, 0]))
print(sol.hIndex([100]))
print(sol.hIndex([50, 100]))
