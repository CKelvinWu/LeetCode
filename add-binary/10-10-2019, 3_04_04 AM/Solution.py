// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        c = str(int(a)+int(b))

        result, carry, val = "", 0, 0
        
        for i in range(len(c)):
            val = carry
            val += int(c[-(i+1)])
            carry, val = val // 2, val % 2
            result += str(val) 
        if carry > 0:
            result += str(1)
        return result[::-1]