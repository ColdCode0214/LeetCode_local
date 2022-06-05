class Solution {
public:
    int minCount(vector<int>& coins) {
		int ans=0;
        int lens=coins.size();
        for(int i=0;i<lens;i++)
        {
			ans+=(coins[i]+1)/2;
		}
        return ans;
    }
};
