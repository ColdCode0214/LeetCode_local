class Solution {
public:
    bool isSubsequence(string s, string t) {
        int lens_s=s.size(), lens_t=t.size();
        if(lens_s==0)
            return true;
        if(lens_s>lens_t)
            return false;
        int point=0;
        for(int i=0;i<lens_t;i++)
        {
            if(t[i]==s[point])
                point++;
            if(point==lens_s)
                return true;
            if(lens_t-1-i<lens_s-1-point)
                return false;
        }
        return false;
    }
};
