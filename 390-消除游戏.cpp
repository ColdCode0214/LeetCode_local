class Solution {
public:
    int lastRemaining(int n) {
        int a1=1, step=1, cnt=n;
        int k=0;
        //for(int i=0;i<k;i++)
        while(cnt>1)
        {
            if(k%2==0)
            {
                a1+=step;
            }
            else
                if(cnt%2==1)
                    a1+=step;
            cnt/=2;
            step*=2;
            k++;
        }
        return a1;
    }
};
