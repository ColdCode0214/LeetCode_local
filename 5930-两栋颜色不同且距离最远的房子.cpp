class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int lens=colors.size();
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            for(int j=lens-1;j>i;j--)
            {
                if(colors[i]!=colors[j])
                    ans=max(ans, j-i);
            }
        }
        return ans;
    }
};
