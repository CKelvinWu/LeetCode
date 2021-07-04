// https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        
        sub = len(haystack)-len(needle)
        
        for i in range(sub+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
            