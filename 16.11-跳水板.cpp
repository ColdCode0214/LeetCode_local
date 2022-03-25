class Solution {
public:
    vector<int> divingBoard(int shorter, int longer, int k) {
        vector<int> ans;
        if(k==0)
            return ans;
        int count=0;
        while(count<=k)
        {
            ans.push_back(shorter*(k-count)+longer*count);
            count++;
        }
        ans.resize(unique(ans.begin(), ans.end())-ans.begin());
        return ans;
    }
};
