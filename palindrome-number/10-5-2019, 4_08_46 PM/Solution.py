// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 :
            return False
        
        a = abs(x)
        num = 0
        while (a != 0):
            temp = a % 10
            num = num * 10 + temp
            a //= 10
            
        if x >= 0 and num == x:
            return True
        else:
            return False
        