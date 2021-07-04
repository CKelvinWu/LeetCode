// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        root = head
        while head:
            length += 1
            head = head.next
        mid = length // 2
        for i in range(mid):
            root = root.next
        return root