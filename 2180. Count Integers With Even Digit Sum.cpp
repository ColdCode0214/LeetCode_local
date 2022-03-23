class Solution {
public:
    int countEven(int num) {
        int ans=0;
        for(int i=1;i<=num;i++)
        {
            int j=i;
            int temp=0;
            while(j>0)
            {
                temp+=j%10;
                j/=10;
            }
            if(temp%2==0)
                ans++;
        }
        return ans;
    }
};
