class Solution {
public:
    bool canPermutePalindrome(string s) {
        int lens=s.size();
        unordered_map<char, int> mp;
        for(auto& a:s)
        {
            mp[a]++;
        }
        int count=0;
        for(auto& a:mp)
        {
            if(a.second%2==1)
            {
                if(count==0)
                    count=1;
                else
                    return false;
            }
        }
        return true;
    }
};
