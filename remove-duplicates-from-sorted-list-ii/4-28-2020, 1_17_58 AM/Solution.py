// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        pre = dummy = ListNode(0)
        cur = post = head
        pre.next = head
        post = head.next
        
        while post:
            while post and cur.val != post.val:
                post = post.next
                cur = cur.next
                pre = pre.next
            while post and cur.val == post.val:
                post = post.next
            if post != cur.next:
                cur = post
                pre.next = post                
                if post is not None:
                    post = post.next
        return dummy.next