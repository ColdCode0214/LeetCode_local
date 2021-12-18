class Solution {
public:
    int getKthMagicNumber(int k) {
        if(k==0)
            return 0;
        int ans[k];
        ans[0]=1;
        int p3=0, p5=0, p7=0;
        int a3, a5, a7;
        for(int i=1;i<k;i++)
        {
            a3=ans[p3]*3;
            a5=ans[p5]*5;
            a7=ans[p7]*7;
            ans[i]=min(min(a3, a5), a7);
            if(ans[i]==a3)
                p3++;
            if(ans[i]==a5)
                p5++;
            if(ans[i]==a7)
                p7++;
        }
        return ans[k-1];
    }
};
