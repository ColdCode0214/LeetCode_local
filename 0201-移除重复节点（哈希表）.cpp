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
    ListNode* removeDuplicateNodes(ListNode* head) {
        if(head==nullptr)
            return head;
        ListNode* pos=head;
        unordered_set<int> occured={head->val};
        while(pos->next)
        {
            ListNode* cur=pos->next;
            if(!occured.count(cur->val))
            {
                occured.insert(cur->val);
                pos=pos->next;
            }
            else
                pos->next=pos->next->next;
        }
        return head;
    }
};
