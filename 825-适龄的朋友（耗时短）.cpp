class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        int cnt[121]{};
        for (int age: ages) {
            ++cnt[age];
        }
        int pre[121]{};
        for (int i = 1,x=0; i <= 120; ++i) {
            pre[i] = x+= cnt[i];
        }
        int ans = 0;
        for (int i = 15; i <= 120; ++i) {
            
                int bound = (i>>1) + 8;
                ans += cnt[i] * (pre[i] - pre[bound - 1] - 1);
            
        }
        return ans;
    }
};