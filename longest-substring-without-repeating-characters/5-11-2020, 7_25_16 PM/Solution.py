// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        memlist = []
        maxlen = 0
        
        for x in s:
            if x in memlist:
                memlist = memlist[memlist.index(x)+1:]
                
            memlist.append(x)
            maxlen = max(maxlen, len(memlist))
        return maxlen;