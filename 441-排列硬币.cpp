class Solution {
public:
    int arrangeCoins(int n) {
        return (-1+sqrt((long long)8*n+1))/2;
    }
};
