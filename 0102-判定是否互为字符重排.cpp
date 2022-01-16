class Solution {
public:
    bool CheckPermutation(string s1, string s2) {
        int l1=s1.size(), l2=s2.size();
        if(l1!=l2)
            return false;
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        for(int i=0;i<l1;i++)
        {
            if(s1[i]!=s2[i])
                return false;
        }
        return true;
    }
};
