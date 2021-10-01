class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int lens_r = ransomNote.size();
        int lens_m = magazine.size();
        if(lens_m<lens_r)
            return false;
        int flag[lens_m];
        for(int i=0;i<lens_m;i++)
            flag[i] = 0;
        int flag1 = 0;
        for(int i=0;i<lens_r;i++)
        {
            flag1 = 0;
            for(int j=0;j<lens_m;j++)
            {
                if(ransomNote[i] == magazine[j] && flag[j] == 0)
                {
                    flag[j] = 1;
                    flag1 = 1;
                    break;
                }
            }
            if(flag1 == 0)
                return false;
        }
        return true;
    }
};
