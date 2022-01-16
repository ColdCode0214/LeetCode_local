class Solution {
public:
    int compress(vector<char>& chars) {
        int lens=chars.size();
        string s="";
        s+=chars[0];
        if(lens==1)
            return 1;
        int index=0;
        for(int i=1;i<lens;i++)
        {
            if(chars[i]!=s[s.size()-1])
            {
                if(i-index>1)
                {
                    s+=to_string(i-index);
                }
                s+=chars[i];
                index=i;
            }
            else if(i==lens-1)
                s+=to_string(lens-1-index+1);
        }
        for(int i=0;i<s.size();i++)
        {
            chars[i]=s[i];
        }
        //cout<<s<<endl;
        //cout<<"size:"<<s.size();
        return s.size();
    }
};
