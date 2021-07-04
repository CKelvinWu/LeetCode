// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool: 
        
        stack = []
        lookup = {"(" : ")", "[" : "]", "{" : "}"}        
        
        for p in s:
            if p in lookup:
                stack.append(p)
            elif len(stack) == 0 or lookup[stack.pop()] != p:
                return False
            # print("stack = ",stack,"p = ",p,stack.pop())
        
        return len(stack) == 0
        
        # while (s != ""): 
        #     if "()" in s:
        #         s = s.replace("()","")
        #     elif "[]" in s:
        #         s = s.replace("[]","")
        #     elif "{}" in s:
        #         s = s.replace("{}","")
        #     elif s == "":
        #         return True
        #     else:
        #         return False
        # return True
    
    