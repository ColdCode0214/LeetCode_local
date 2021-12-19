class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int lens=heights.size();
        if(lens==0)
            return 0;
        int expected[lens];
        for(int i=0;i<lens;i++)
            expected[i]=heights[i];
        sort(heights.begin(), heights.end());
        int ans=0;
        for(int i=0;i<lens;i++)
            if(heights[i]!=expected[i])
                ans++;
        return ans;
    }
};
