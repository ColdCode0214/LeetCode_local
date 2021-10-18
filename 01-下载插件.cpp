class Solution {
public:
    int leastMinutes(int n) {
        return ceil(log2(n))+1;
    }
};
