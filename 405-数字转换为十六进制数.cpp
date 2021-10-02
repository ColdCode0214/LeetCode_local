class Solution {
public:
    string toHex(int num) {
        if(num == -2147483648)
            return "80000000";
        string key[16];
        key[0]='0'; key[1]='1'; key[2]='2'; key[3]='3'; 
        key[4]='4'; key[5]='5'; key[6]='6'; key[7]='7'; 
        key[8]='8'; key[9]='9'; key[10]='a'; key[11]='b'; 
        key[12]='c'; key[13]='d'; key[14]='e'; key[15]='f';

        string ans="";
        int temp;
        if(num>=0)
        {
            while(num>=16)
            {
                ans=key[num%16]+ans;
                num/=16;
            }
            ans=key[num]+ans;
            return ans;
        }
        else
        {
            num=-num;
            int jinwei=0;
            while(num>=16)
            {
                if(jinwei==0)
                {
                    if(num%16==0)
                        ans = key[0]+ans;   
                    else
                        ans = key[16-num%16]+ans;
                }
                else
                    ans = key[15-num%16]+ans;
                if(num%16 != 0)
                    jinwei=1;
                num/=16;
            }
            if(jinwei==0)
                ans = key[16-num%16]+ans;
            else
                ans = key[15-num%16]+ans;
            temp=ans.size();
            if(temp<8)
            {
                for(int i=0;i<8-temp;i++)
                    ans = "f"+ans;
            }
            return ans;
        }
        
    }
};
