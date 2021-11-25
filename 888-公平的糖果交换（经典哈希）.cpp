class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        int sumA=accumulate(aliceSizes.begin(), aliceSizes.end(),0);
        int sumB=accumulate(bobSizes.begin(), bobSizes.end(), 0);
        int delta=(sumA-sumB)/2;
        unordered_set<int> rec(aliceSizes.begin(), aliceSizes.end());
        vector<int> ans;
        for(auto& y:bobSizes)
        {
            int x=y+delta;
            if(rec.count(x))
            {
                ans=vector<int>{x,y};
                break;
            }
        }
        return ans;
    }
};
