// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        
        
        n, Pascal, ans = 1, [1], [[1]]
        
        while n < numRows :
            result = []
            n += 1
            result.append(1)
            for i in range(len(Pascal)-1):
                result.append(Pascal[i]+Pascal[i+1])
            result.append(1)
            Pascal = result
            ans.append(result)
        return ans
        