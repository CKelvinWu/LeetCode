// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        Pascal = [1]
        while len(Pascal) < rowIndex + 1:
            
            for i in range(len(Pascal)-1):
                Pascal.append(Pascal[0] + Pascal[1])
                Pascal.pop(0)
            Pascal.append(1)
        return Pascal