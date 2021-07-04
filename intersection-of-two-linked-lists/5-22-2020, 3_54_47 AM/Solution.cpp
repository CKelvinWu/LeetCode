// https://leetcode.com/problems/intersection-of-two-linked-lists

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *dummyA = headA, *dummyB = headB;
        if (dummyA == NULL || dummyB == NULL) return NULL;
        
        while (dummyA != NULL && dummyB != NULL && dummyA != dummyB){
            
            dummyA = dummyA->next;
            dummyB = dummyB->next;            
            if (dummyA == dummyB) return dummyA;
            if (dummyA == NULL) dummyA = headB;
            if (dummyB == NULL) dummyB = headA;
        }
        return dummyA;
    }
};