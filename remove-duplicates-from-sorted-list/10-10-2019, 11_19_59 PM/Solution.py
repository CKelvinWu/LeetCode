// https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        # while curr:
        #     runner = curr.next
        #     while runner and runner.val == curr.val:
        #         runner = runner.next
        #     curr.next = runner
        #     curr = curr.next
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
            
        return head
        
        
        
        
        # curr = dummy = ListNode(0)
        # curr.next = head
        # curr = curr.next
        # while head:             
        #     if head.val > curr.val:
        #         curr.next = head
        #         curr = curr.next
        #     head = head.next
        #     if head == None:
        #         curr.next = None
        # return dummy.next
            