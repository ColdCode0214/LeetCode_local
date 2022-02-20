class Solution {
public:
    long long smallestNumber(long long num) {
        vector<int> n;
        if(num==0)
            return 0;
        int flag=0;//标记是否为负数
        if(num<0)
        {
            flag=1;
            num=-num;
        }
        while(num>0)
        {
            n.push_back(num%10);
            num/=10;
        }
        sort(n.begin(), n.end());
        long long ans=0;
        int lens=n.size();
        if(flag==1)
        {
            for(int i=lens-1;i>=0;i--)
            {
                ans*=10;
                ans+=n[i];
            }
            return -ans;            
        }
        else
        {
            for(int i=0;i<lens;i++)
            {
                if(n[i]!=0)
                {
                    swap(n[0], n[i]);
                    break;
                }
            }
            for(int i=0;i<lens;i++)
            {
                ans*=10;
                ans+=n[i];
            }
        }
        return ans;
    }
};
