class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        if(bills[0]!=5)
            return false;
        int lens=bills.size();
        if(lens==1)
            return true;
        bool ans=true;
        bool temp=false;//记录付款为10元时是否能找到1张5元
        bool temp1=false,temp2=false;//记录付款为20时能否找到1张5元和1张10元
        bool temp3=false;//如果找不到1张5元和一张10元就改找3张5元，此时temp2改为记录能否找到第二张5元，temp3记录能否找到第三张5元
        vector<int> wallet;
        wallet.push_back(5);
        for(int i=1;i<lens;i++)
        {
            temp=false,temp1=false,temp2=false,temp3=false;
            if(bills[i]==10)
            {
                for(int j=0;j<i;j++)
                {
                    if(bills[j]==5&&temp==false)
                    {
                        bills[j]=0;
                        temp=true;
                        break;
                    }
                }
                if(temp==false)
                {
                    ans=false;
                    break;
                }
            }
            if(bills[i]==20)
            {
                temp=false;
                for(int j=0;j<i;j++)
                {
                    if(bills[j]==5&&temp1==false)
                    {
                        bills[j]=0;
                        temp1=true;
                    }
                    if(bills[j]==10&&temp2==false)
                    {
                        bills[j]=0;
                        temp2=true;
                    }
                    if(temp1==true&&temp2==true)
                    {
                        temp=true;
                        break;
                    }
                }
                if(temp1==false)
                {
                    ans=false;
                    break;
                }
                if(temp2==false)
                {
                    for(int j=0;j<i;j++)
                    {
                        if(bills[j]==5&&temp2==false)
                        {
                            temp2=true;
                            bills[j]=0;
                        }
                        if(bills[j]==5&&temp3==false)
                        {
                            temp3=true;
                            bills[j]=0;
                        }
                        if(temp2==true&&temp3==true)
                        {
                            temp=true;
                            break;
                        }
                    }
                }
                if(temp==false)
                {
                    ans=false;
                    break;
                }
            }
            if(ans==false)
                break;
        }
        return ans;
    }
};