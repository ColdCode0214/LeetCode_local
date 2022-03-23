class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int lens=words.size();
        int l2=pref.size();
        int flag=0;
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            flag=0;
            for(int j=0;j<l2;j++)
            {
                if(words[i][j]!=pref[j])
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
                ans++;
        }
        return ans;
    }
};
