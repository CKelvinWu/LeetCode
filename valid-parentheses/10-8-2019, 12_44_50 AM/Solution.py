// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool: 
        # while (s != ""): 
        #     result = False            
        #     for i in range(len(s)-1):
        #         k = 0                 
        #         if  ((s[i] == "(" and s[i+1] == ")") or (s[i] == "[" and s[i+1] == "]") or (s[i] == "{" and s[i+1] == "}")):
        #             s = s.replace(s[i] + s[i+1], "")
        #             result = True
        #             break
        #     if s == "":
        #         return True            
        #     elif result == False or len(s) <= 1:
        #         return False
        # return True
        
        while (s != ""): 
            
            if s == "":
                return True 
            elif "()" in s:
                s = s.replace("()","")
                continue
            elif "[]" in s:
                s = s.replace("[]","")
                continue
            elif "{}" in s:
                s = s.replace("{}","")
                continue
            elif s == "":
                return True            
            else:
                return False
        return True