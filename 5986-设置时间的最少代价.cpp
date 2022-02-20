class Solution {
public:
    int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        int min=targetSeconds/60, s=targetSeconds%60;
        if(min>99)
        {
            min--;
            s+=60;
        }
        vector<int> n1;
        n1.push_back(min/10);
        n1.push_back(min%10);
        n1.push_back(s/10);
        n1.push_back(s%10);
        min--;
        s+=60;
        vector<int> n2;
        n2.push_back(min/10);
        n2.push_back(min%10);
        n2.push_back(s/10);
        n2.push_back(s%10);
        //for(int i=0;i<4;i++)
            //cout<<n2[i]<<" ";
        //cout<<endl;
        
        int a1=0, a2=0;
        int f1=0, f2=0;
        int temp=startAt;
        for(int i=0;i<4;i++)
        {
            if((n1[i]==0 && f1==1) || n1[i]!=0)
            {
                if(n1[i]==startAt)
                {
                    a1+=pushCost;
                }
                else
                {
                    a1+=moveCost;
                    a1+=pushCost;
                    startAt=n1[i];
                }
                f1=1;
            }
        }
        startAt=temp;
        for(int i=0;i<4;i++)
        {
            if((n2[i]==0 && f2==1) || n2[i]!=0)
            {
                if(n2[i]==startAt)
                {
                    a2+=pushCost;
                    //cout<<"####";
                }
                else
                {
                    a2+=moveCost;
                    a2+=pushCost;
                    startAt=n2[i];
                }
                f2=1;
            }
        }
        //cout<<"a1:"<<a1<<" a2:"<<a2<<endl;
        if(s<=99)
        {
            if(a1<=a2)
                return a1;
            else
                return a2;
        }
        else
            return a1;
    }
};
