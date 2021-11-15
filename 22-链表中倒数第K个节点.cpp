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
    ListNode* getKthFromEnd(ListNode* head, int k) {
        if(head==nullptr)
            return head;
        int count=0;
        ListNode* cur=head;
        while(cur)
        {
            count++;
            cur=cur->next;
        }
        cur=head;
        for(int i=0;i<count-k;i++)
            cur=cur->next;
        return cur;
    }
};
