class Solution {
public:
    bool isPalindrome(string s) {
        int lens=s.size();
        if(lens==0)
            return true;
        int l=0, r=lens-1;
        for(int i=0;i<lens;i++)
            s[i]=tolower(s[i]);
        while(l<r)
        {
            if(((s[l]>=48 && s[l]<=57) || (s[l]>=97 && s[l]<=122)) && ((s[r]>=48 && s[r]<=57) || (s[r]>=97 && s[r]<=122)))
            {
                if(s[l]!=s[r])
                    return false;
                r--;
                l++;
            }

            else if(!((s[l]>=48 && s[l]<=57) || (s[l]>=97 && s[l]<=122)))
                l++;
            else if(!((s[r]>=48 && s[r]<=57) || (s[r]>=97 && s[r]<=122)))
                r--;
        }
        return true;
    }
};
