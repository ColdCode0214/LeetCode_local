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
        vector<int> arr;
        ListNode* pre=head;
        ListNode* cur=pre->next;
        arr.push_back(pre->val);
        int flag=0;
        while(cur)
        {
            flag=0;
            for(int i=0;i<arr.size();i++)
            {
                if(cur->val==arr[i])
                {
                    if(cur->next!=nullptr)
                        pre->next=cur->next;
                    else
                        pre->next=nullptr;
                    flag=1;
                    break;
                }
                
            }
            if(flag==0)
            {
                arr.push_back(cur->val);
                pre=cur;
            }
            cur=cur->next;
        }
        return head;
    }
};
