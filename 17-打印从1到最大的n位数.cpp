class Solution {
public:
    vector<int> printNumbers(int n) {
        int count=0;
        vector<int> ans;
        for(int i=0;i<n;i++)
            count=count*10+9;
        for(int i=1;i<=count;i++)
            ans.push_back(i);
        return ans;
    }
};
