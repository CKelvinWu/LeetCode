// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        Pascal = []
        for i in range(rowIndex + 1):
            result = []
            for j in range(i+1):
                if j in [0,i]:
                    result.append(1)
                else:
                    result.append(Pascal[j-1] + Pascal[j])
            Pascal = result
        return result