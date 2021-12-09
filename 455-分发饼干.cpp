class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int ans=0;
        int index=s.size()-1;
        for(int i=g.size()-1;i>=0;i--)
        {
            for(int j=index;j>=0;j--)
            {
                if(s[j]>=g[i])
                {
                    ans++;
                    index=j-1;
                    break;
                }
            }
        }
        return ans;
    }
};
