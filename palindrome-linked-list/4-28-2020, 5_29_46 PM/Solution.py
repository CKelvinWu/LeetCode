// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow = slow.next
        slow = self.reverseList(slow)
        
        while slow:
            if head.val != slow.val: return False
            slow = slow.next
            head = head.next
        return True
        
        
        
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
            
        return prev