// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        
        root = prev = ListNode(0)
        curr = head
        
        while curr and curr.next:
            
            post = curr.next.next
            curr.next.next = curr            
            prev.next = curr.next
            prev = curr
            curr.next = post
            curr = curr.next
            
        return root.next