class Solution {
public:
    string convertToBase7(int num) {
        if(num==0)
            return "0";
        string ans="";
        string temp;
        int flag=1;
        if(num<0)
        {
            flag=-1;
            num=-num;
        }
            
        while(num>0)
        {
            temp=num%7+48;
            ans=temp+ans;
            num/=7;
        }
        if(flag==-1)
            ans='-'+ans;
        return ans;
    }
};
