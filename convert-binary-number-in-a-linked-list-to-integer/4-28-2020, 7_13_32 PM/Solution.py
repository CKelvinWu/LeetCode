// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.reverse()
        
        ans = 0
        for i in range(len(arr)):
            ans += arr[i]*2**i
        return ans