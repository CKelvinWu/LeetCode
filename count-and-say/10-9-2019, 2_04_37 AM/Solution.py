// https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
            
        s = "11"
        
        i = 0
        while i < n-2:
            news = ""
            count = 1
            for j in range(len(s)):                
                if j == len(s)-1:
                    news += str(count)+s[j]
                elif s[j] == s[j+1]:
                    count += 1
                else:
                    news += str(count)+s[j]
                    count = 1
                
            i += 1
            s = news
        return s
                
            
        