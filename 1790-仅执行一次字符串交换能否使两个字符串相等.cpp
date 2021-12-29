class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int lens=s1.size();
        int count=0;
        string a1, a2, b1, b2;
        for(int i=0;i<lens;i++)
        {
            if(s1[i]!=s2[i] && count==0)
            {
                count++;
                a1=s1[i];
                b1=s2[i];
            }
            else if(s1[i]!=s2[i] && count==1)
            {
                count++;
                a2=s1[i];
                b2=s2[i];
            }
            else if(s1[i]!=s2[i])
                return false;
        }
        if(count==1 || (a1!=b2 || a2!=b1))
        {
            return false;
        }
            
        return true;
    }
};
