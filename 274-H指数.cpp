class Solution {
public:
    int hIndex(vector<int>& citations) {
        int lens=citations.size();
        sort(citations.begin(), citations.end());
        if((lens==1 && citations[0]==0) || citations[lens-1]==0)
            return 0;
        for(int i=min(citations[lens-1], lens);i>=0;i--)
        {
            if(citations[lens-i]>=i)
                return i;
        }
        return 0;
    }
};
