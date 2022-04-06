class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans=0;
        string s="";
        string g="";
        string temp="";
        // vector<int> s;
        // vector<int> g;
        
        while(start>0)
        {
            temp=start%2+48;
            s+=temp;
            start/=2;
        }
        while(goal>0)
        {
            temp=goal%2+48;
            g+=temp;
            goal/=2;
        }
        //cout<<"s:"<<s<<endl;
        //cout<<"g:"<<g<<endl;
        int ls=s.size();
        int lg=g.size();
        int index=0;
        while(index<ls && index<lg)
        {
            if(s[index]!=g[index])
            {
                ans++;
            }
            index++;
        }
        if(index<ls)
        {
            while(index<ls)
            {
                if(s[index]=='1')
                    ans++;
                index++;
            }
        }
        if(index<lg)
        {
            while(index<lg)
            {
                if(g[index]=='1')
                    ans++;
                index++;
            }
        }
        return ans;
    }
};
