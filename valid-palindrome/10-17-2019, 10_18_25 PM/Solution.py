// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        start, end = 0, len(s)-1
        while start < end:
            if s[start].isalnum() is False:
                start += 1
            elif s[end].isalnum() is False:
                end -= 1
            elif s[start] == s[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
            
        return True
            
                