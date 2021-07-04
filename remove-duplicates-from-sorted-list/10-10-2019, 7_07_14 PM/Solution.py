// https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        curr = dummy = ListNode(0)
        curr.next = head
        curr = curr.next
        while head:             
            if head.val > curr.val:
                curr.next = head
                curr = curr.next
            head = head.next
            if head == None:
                curr.next = None
            
        
        return dummy.next
            