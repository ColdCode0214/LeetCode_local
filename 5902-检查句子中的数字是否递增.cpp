class Solution {
public:
    bool areNumbersAscending(string s) {
        int lens=s.size();
        int pre=-1;
        int now=0;
        int count=0;
        string num="";
        for(int i=0;i<lens;i++)
        {
            if(s[i]>=48 && s[i]<=57)
            {
                num+=s[i];
                //cout<<"num:"<<num<<endl;
            }
            if((s[i]==' ' && (s[i-1]>=48 && s[i-1]<=57)) || ((i==lens-1) && s[i]>=48 && s[i]<=57))
            {
                now=0;
                int l2=num.size();
                for(int j=0;j<l2;j++)
                    now+=(num[j]-48)*pow(10,l2-1-j);
                //cout<<"now:"<<now<<" pre:"<<pre<<endl;
                if(now<=pre)
                    return false;
                pre=now;
                num="";
            }
        }
        return true;
    }
};
