// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        Pascal = [1] + [0] * rowIndex
        
        for i in range(rowIndex):
            Pascal[0] = 1
            for j in range(i+1, 0, -1):
                Pascal[j] = Pascal[j] + Pascal[j-1]
        
        return Pascal