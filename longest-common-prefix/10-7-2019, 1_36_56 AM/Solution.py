// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        

        
        for i in range(len(strs[0])):
            same = strs[0][i]
            print(i,same)
            for j in strs[1:]:
                if i >= len(j) or same != j[i] :
                    return strs[0][:i]
        else:
            return strs[0]