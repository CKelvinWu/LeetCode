// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if not s:
            return 0
        elif " " not in s:
            return len(s)

        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                count += 1
            elif s[i] == " " and count > 0:
                return count            
        return count
        
            