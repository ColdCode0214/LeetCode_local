class Solution {
public:
    int longestPalindrome(string s) {
        int lens=s.size();
        int ans=0;
        unordered_map<char, int> mp;
        for(auto& a:s)
        {
            mp[a]++;
            //cout<<mp[a]<<" ";
        }
        int flag=0;
        for(auto& a:mp)
        {
            if(a.second%2==0)
                ans+=a.second;
            else
            {
                if(flag==0)
                {
                    ans+=a.second;
                    flag=1;
                }
                else
                    ans+=(a.second-1);
            }
        }
        return ans;
    }
};
