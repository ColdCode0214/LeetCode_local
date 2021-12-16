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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==nullptr && l2==nullptr)
            return l1;
        if(l1==nullptr)
            return l2;
        if(l2==nullptr)
            return l1;
        ListNode* p1=l1;
        ListNode* p2=l2;
        ListNode* head=new ListNode();
        //head->val=0;
        //head->next=nullptr;
        ListNode* cur=head;
        while(p1 && p2)
        {
            if(p1->val <= p2->val)
            {
                cur->next=p1;
                p1=p1->next;
            }
            else
            {
                cur->next=p2;
                p2=p2->next;
            }
            cur=cur->next;
        }
        if(p1)
        {
            cur->next=p1;
        }
        if(p2)
        {
            cur->next=p2;
        }
        return head->next;
    }
};
