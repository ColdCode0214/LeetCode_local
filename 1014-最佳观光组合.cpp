class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int m1=0;
        int ans=0;
        int lens=values.size();
        for(int i=0;i<lens;i++)
        {
            ans=max(ans, m1+values[i]-i);
            m1=max(m1, values[i]+i);
        }
        return ans;
    }
};
