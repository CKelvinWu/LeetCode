// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# iteratively:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     curr, prev = head, None
    #     while curr:    
    #         post = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = post
    #     return prev
# recursively:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head        
        new = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new
        
        