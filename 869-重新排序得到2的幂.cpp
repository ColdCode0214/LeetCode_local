class Solution {
public:
    bool reorderedPowerOf2(int n) {
        if(n==1000000000)
            return false;
        vector<int> table[9];
        for(int i=0;i<30;i++)
        {
            if(i<=3)
                table[0].push_back(pow(2,i));
            else if(i<=6)
                table[1].push_back(pow(2,i));
            else if(i<=9)
                table[2].push_back(pow(2,i));
            else if(i<=13)
                table[3].push_back(pow(2,i));
            else if(i<=16)
                table[4].push_back(pow(2,i));
            else if(i<=19)
                table[5].push_back(pow(2,i));
            else if(i<=23)
                table[6].push_back(pow(2,i));
            else if(i<=26)
                table[7].push_back(pow(2,i));
            else if(i<=29)
                table[8].push_back(pow(2,i));
        }
        vector<int> num;
        while(n>0)
        {
            num.push_back(n%10);
            n/=10;
        }

        int lens=num.size();
        
        int flag[lens];
        for(int i=0;i<lens;i++)
            flag[i]=0;

        int count=0;

        for(int i=0;i<table[lens-1].size();i++)
        {
            for(int i=0;i<lens;i++)
                flag[i]=0;
            count=0;
            vector<int> compare;
            while(table[lens-1][i]>0)
            {
                compare.push_back(table[lens-1][i]%10);
                table[lens-1][i]/=10;
            }
            for(int j=0;j<lens;j++)
            {
                for(int k=0;k<lens;k++)
                {
                    if(num[k]==compare[j] && flag[k]==0)
                    {
                        count++;
                        flag[k]=1;
                        break;
                    }
                }
            }
            if(count==lens)
                return true;
        }
        return false;
    }
};
