class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int m=bank.size(), n=bank[0].size();
        int pre=0,cur=0;
        int ans=0;
        for(int i=0;i<m;i++)
        {
            cur=0;
            for(int j=0;j<n;j++)
            {
                if(bank[i][j]=='1')
                {
                    cur++;
                }
            }
            ans+=cur*pre;
            if(cur!=0)
                pre=cur;
        }
        return ans;
    }
};
