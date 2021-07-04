// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        num = 0
        while(a != 0):
            temp = a % 10
            num = num * 10 + temp
            a //= 10
        if x < 0 and num <= 2**31 - 1:
            return -num
        elif x > 0 and num <= 2**31:
            return num
        else:
            return 0