// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # if not strs:
        #     return ""
        # for i in range(len(strs[0])):
        #     same = strs[0][i]
        #     for j in strs[1:]:
        #         if i >= len(j) or same != j[i] :
        #             return strs[0][:i]
        # else:
        #     return strs[0]
        
        
        result = ""
        i = 0
        
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
                
            except Exception as e:
                break
        return result