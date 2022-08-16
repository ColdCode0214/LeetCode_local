class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int n=nums.size();
        unordered_set<int> st;
        for(int x:nums)
            st.insert(x);
        int ans=0;
        for(int a:nums)
            if(st.count(a-diff)>0 && st.count(a+diff)>0)
                ans++;
        return ans;
    }
};
