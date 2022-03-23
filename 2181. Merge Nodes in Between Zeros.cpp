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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* cur=head->next;
        //ListNode* ans=head->next;

        while(cur)
        {
            if(cur->val==0)
                cur=cur->next;
            else
            {
                if(cur->next->val==0)
                {
                    cur->next=cur->next->next;
                    cur=cur->next;
                }
                else
                {
                    cur->val+=cur->next->val;
                    cur->next=cur->next->next;
                }
            }
        }
        return head->next;
    }
};
