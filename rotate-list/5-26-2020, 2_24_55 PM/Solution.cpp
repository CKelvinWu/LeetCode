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
        ListNode *curr = head;
        int len = 0;
        while (curr) {
            curr = curr->next;
            len++;
        }
        
        k = k%len;
        if (k == 0) return head;
        ListNode *fast = head, *slow = head;
        
        for (int i = 0; i < k; i++){
            fast = fast->next;
        }
        while(fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        curr = slow->next;
        slow->next = NULL;
        fast->next = head;
        return curr;
    }
};