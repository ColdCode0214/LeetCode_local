class Solution {
public:
    int arrangeCoins(int n) {
        int left=1, right=n;
        
        while(left<right)
        {
            int mid=(right-left+1)/2+left;
            if((long long)mid*(mid+1)<=(long long)n*2)
                left=mid;
            else
                right=mid-1;
        }
        return left;
    }
};
