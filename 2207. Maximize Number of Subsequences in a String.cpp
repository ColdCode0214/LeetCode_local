class Solution {
public:
    long long maximumSubsequenceCount(string text, string pattern) {
        long long int ans=0;
        int lens=text.size();
        if(pattern[0]==pattern[1])
        {
            int count=0;
            for(int i=0;i<lens;i++)
            {
                if(text[i]==pattern[0])
                    count++;
            }
            ans=1LL*(1+(count-1))*(count-1)/2;
        }
        long long int num[2];
        num[0]=0, num[1]=0;
        for(int i=0;i<lens;i++)
        {
            if(text[i]==pattern[0])
                num[0]++;
            else if(text[i]==pattern[1])
            {
                num[1]++;
                ans+=num[0];
            }
                
        }
        if(num[0]<=num[1])
            ans+=num[1];
        else
            ans+=num[0];
        return ans;
    }
};
