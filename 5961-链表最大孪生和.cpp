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
    int pairSum(ListNode* head) {
        vector<int> temp;
        ListNode* cur=head;
        while(cur)
        {
            temp.push_back(cur->val);
            cur=cur->next;
        }
        int ans=0;
        int lens=temp.size();
        for(int i=0;i<lens/2;i++)
        {
            ans=max(ans, temp[i]+temp[lens-1-i]);
        }
        return ans;    
    }
};
