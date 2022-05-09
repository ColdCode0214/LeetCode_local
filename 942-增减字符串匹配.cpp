class Solution {
public:
    vector<int> diStringMatch(string s) {
        int lens=s.size();
        int l=0, r=lens;
        vector<int> ans;
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='I')
            {
                ans.push_back(l);
                l++;
            }
            else
            {
                ans.push_back(r);
                r--;
            }
        }
        //cout<<"r:"<<r<<" l:"<<l<<endl;
        ans.push_back(r);
        return ans;
    }
};
