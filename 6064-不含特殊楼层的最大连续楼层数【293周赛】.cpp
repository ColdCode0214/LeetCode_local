class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        int lens=special.size();
        sort(special.begin(), special.end());
        int ans=0;
        ans=max(special[0]-bottom, top-special[lens-1]);
        for(int i=0;i<lens-1;i++)
        {
            ans=max(ans, special[i+1]-special[i]-1);
        }
        return ans;
    }
};
