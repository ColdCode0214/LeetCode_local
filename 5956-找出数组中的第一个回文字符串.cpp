class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        int lens=words.size();
        string ans="";
        int flag=0;
        for(int i=0;i<lens;i++)
        {
            flag=0;
            int lens2=words[i].size();
            //cout<<"size():"<<lens2<<endl;
            //cout<<"flag1:"<<flag<<endl;
            for(int j=0;j<lens2/2;j++)
            {
                if(words[i][j]!=words[i][lens2-1-j])
                {
                    flag=1;
                    break;
                }
                    
            }
            //cout<<"flag:"<<flag<<endl;
            if(flag==0)
            {
                return words[i];
            }
                //ans=words[i];
        }
        return ans;
    }
};
