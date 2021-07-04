// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        j, result = 0, 0
        for i in reversed(s):
            result += (ord(i)-ord("A")+1)*26**j
            j += 1
        return result