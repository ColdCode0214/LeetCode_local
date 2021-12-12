class Solution {
public:
    bool isUnique(string astr) {
        sort(astr.begin(), astr.end());
        int lens=astr.size();
        for(int i=0;i<lens-1;i++)
            if(astr[i]==astr[i+1])
                return false;
        return true;
    }
};
