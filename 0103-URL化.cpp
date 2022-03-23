class Solution {
public:
    string replaceSpaces(string S, int length) {
        int lens=S.size();
        string ans="";
        string temp="%20";
        for(int i=0;i<lens;i++)
        {
            if(S[i]!=' ')
            {
                ans+=S[i];
            }
            else
            {
                if(i>length-1)
                {
                    //cout<<"i:"<<i<<endl;
                    break;
                }
                   
                else
                    ans+=temp;
            }
        }
        return ans;
    }
};
