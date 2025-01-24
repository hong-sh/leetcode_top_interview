"""
leetcode 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        iters = re.findall("[0-9a-z]+", s)

        content = ""
        for sub_s in iters:
            content += sub_s

        left, right = 0, len(content) - 1
        while left <= right:
            if content[left] != content[right]:
                return False

            left += 1
            right -= 1

        return True


sol = Solution()
# print(sol.isPalindrome(s="A man, a plan, a canal: Panama"))
# print(sol.isPalindrome(s="race a car"))
# print(sol.isPalindrome(s=" "))

print(sol.isPalindrome(s="0P"))
