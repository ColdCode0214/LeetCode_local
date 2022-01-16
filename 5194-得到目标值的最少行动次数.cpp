class Solution {
public:
    int minMoves(int target, int maxDoubles) {
        int ans=0;
        int temp=1;
        while(target!=1)
        {
            if(target%2==1)
            {
                target--;
                ans++;
            }
            else
            {
                if(maxDoubles>0)
                {
                    target/=2;
                    ans++;
                    maxDoubles--;
                }
                else
                {
                    ans+=(target-1);
                    break;
                }
            }
        }
        return ans;
    }
};
