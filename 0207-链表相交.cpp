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
        if(headA==nullptr || headB==nullptr)
            return nullptr;
        ListNode* pa=headA;
        ListNode* pb=headB;
        while(pa || pb)
        {
            if(pa==pb)
                return pa;
            if(pa==nullptr)
                pa=headB;
            else
                pa=pa->next;
            if(pb==nullptr)
                pb=headA;
            else    
                pb=pb->next;
            
        }
        return nullptr;
    }
};
