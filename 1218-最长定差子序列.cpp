class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int lens=arr.size();
        //int dp[lens];
        unordered_map<int, int> dp;
        int ans=1;
        for(int i=0;i<lens;i++)
        {
            dp[arr[i]]=dp[arr[i]-difference]+1;
            ans=max(ans, dp[arr[i]]);
        }
        return ans;
    }
};
