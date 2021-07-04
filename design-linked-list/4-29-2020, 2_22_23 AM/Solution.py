// https://leetcode.com/problems/design-linked-list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index == 0:
            return self.head.val
        else:
            current = self.head
            count = 0
            while current != None:
                if index == count:
                    return current.val
                count += 1
                current = current.next
            return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = ListNode(val)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
        self.size += 1
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = ListNode(val)
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            count = 0
            current = self.head
            prev = None
            newNode = ListNode(val)
            while count != index and current.next != None:
                count += 1
                prev = current
                current = current.next
            if count == index:
                prev.next = newNode 
                newNode.next = current
                self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            ans = self.head.val
            newHead = self.head.next
            self.head = newHead
            self.size -= 1
            return ans
        else:
            count = 0
            current = self.head
            prev = None
            while count != index and current.next != None:
                prev = current
                current = current.next
                count += 1
            if count == index:    
                prev.next = current.next 
                self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)