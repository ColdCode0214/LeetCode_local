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
        ListNode* c1=headA;
        ListNode* c2=headB;
        while(c1!=nullptr && c2!=nullptr)
        {
            if(c1==c2 && c1!=nullptr)
                return c1;
            if(c1->next==nullptr && c2->next==nullptr)
                return nullptr;
            if(c1->next==nullptr)
                c1=headB;
            else
                c1=c1->next;
            if(c2->next==nullptr)
                c2=headA;
            else   
                c2=c2->next;
            
        }
        return nullptr;
    }
};
