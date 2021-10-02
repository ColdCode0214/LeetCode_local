class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        int lens=candyType.size();
        int count=1;
        sort(candyType.begin(),candyType.end());
        for(int i=1;i<lens;i++)
        {
            if(candyType[i]!=candyType[i-1])
                count++;
        }
        return min(count, lens/2);
    }
};
