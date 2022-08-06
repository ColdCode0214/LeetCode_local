class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n=nums.size();
        long long int total=1LL*n*(n-1)/2;
        map<int, int> count;
        for(int i=0;i<n;i++)
        {
            total -= count[i-nums[i]];
            count[i-nums[i]]++;
        }
        return total;
    }
};
