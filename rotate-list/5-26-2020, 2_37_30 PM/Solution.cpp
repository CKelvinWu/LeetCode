// https://leetcode.com/problems/rotate-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;
        ListNode *tail = head;
        ListNode *new_head = head;
        
        int len = 1;
        while (tail->next) {    // count the length of the link
            tail = tail->next;
            len++;
        }
        
        k %= len;
        if (k == 0) return head;        
        
        tail->next = head;  // circle the link
        
        for (int i = 0; i < len-k; i++){
            tail = tail->next;
        }
        new_head = tail->next;
        tail->next = NULL;
        
        return new_head;
    }
};