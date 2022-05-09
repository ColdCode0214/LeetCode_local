class Solution {
public:
    string largestGoodInteger(string num) {
        int lens=num.size();
        string ans="";
        for(int i=0;i<lens-2;i++)
        {
            if(num[i]==num[i+1] && num[i+1]==num[i+2])
            {
                if(ans.size()==0)
                {
                    ans+=num[i];
                    ans+=num[i];
                    ans+=num[i];
                }
                else
                {
                    if(num[i]>ans[0])
                    {
                        ans=num[i];
                        ans+=num[i];
                        ans+=num[i];
                    }
                }
            }
        }
        return ans;
    }
};
