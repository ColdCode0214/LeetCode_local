class Solution {
public:
    int findComplement(int num) {
        string ans="";
        string temp="";
        int sum=0;
        while(num>0)
        {
            temp=num%2+48;
            ans=temp+ans;
            num/=2;
        }
        int lens=ans.size();
        for(int i=0;i<lens;i++)
        {
            if(ans[i]=='1')
                ans[i]='0';
            else
                ans[i]='1';
        }
        int count=0;
        for(int i=lens-1;i>=0;i--)
            sum+=(ans[i]-48)*pow(2,lens-1-i);
        return sum;
    }
};
