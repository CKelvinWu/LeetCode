// https://leetcode.com/problems/palindrome-linked-list

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
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;
        ListNode *fast = head, *slow = head;
        while (fast->next && fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        slow = slow->next;
        slow = reversed(slow);
        
        while (slow){
            if (slow->val != head->val) return false;
            slow = slow->next;
            head = head->next;
        }
        return true;
                
    }
    ListNode *reversed(ListNode* head){
        if (!head || !head->next) return head;
        ListNode *dummy = reversed(head->next);
        head->next->next = head;
        head->next = NULL;
        return dummy;
    }
};