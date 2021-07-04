// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if not s:
            return 0

        count = 0
        for i in range(len(s)-1,-1,-1):
            # print("i",i,s[i-1],count)
            if s[i] != " ":
                count += 1
            elif s[i] == " " and count > 0:
                return count            
        return count
        
            