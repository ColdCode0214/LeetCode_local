class Solution {
public:
    bool canChange(string start, string target) {
        int n=start.size();
        //s, t = '', ''
        string s="", t="";
        vector<int> sl, sr, tl, tr;
        for(int i=0;i<n;i++)
        {
            if(start[i]!='_')
            {
                s+=start[i];
                if(start[i]=='L')
                    sl.push_back(i);
                if(start[i]=='R')
                    sr.push_back(i);
            }
                
            if(target[i]!='_')
            {
                t+=target[i];
                if(target[i]=='L')
                    tl.push_back(i);
                if(target[i]=='R')
                    tr.push_back(i);
            }
                
        }
        //cout<<"s:"<<s<<" t:"<<t<<endl;
        if(s!=t)
        {
            cout<<"1"<<endl;
            return false;
        }
            //return false;
        int lensl=sl.size(), lensr=sr.size();
        for(int i=0;i<lensl;i++)
        {
            if(sl[i]<tl[i])
            {
                return false;
            }
        }
        for(int i=0;i<lensr;i++)
        {
            if(sr[i]>tr[i])
            {
                return false;
            }
        }
        return true;
    }
};
