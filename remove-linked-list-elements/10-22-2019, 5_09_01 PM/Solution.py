// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        result = dummy = ListNode(0)        
        while head:
            if head.val != val:
                result.next = head
                result = result.next     
            else:
                result.next = None
            head = head.next
        return dummy.next