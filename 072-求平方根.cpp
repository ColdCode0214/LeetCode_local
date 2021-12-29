class Solution {
public:
    int mySqrt(int x) {
        int left=0, right=x;
        int mid=0, ans=0;
        while(left<=right)
        {
            mid=left+(right-left)/2;
            if((long long)mid*mid<=x)
            {
                ans=mid;
                left=mid+1;
            }
            else
                right=mid-1;

        }
        return ans;
    }
};
