class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        //sort(stones.begin(),stones.end())
        int lens_j=jewels.size();
        int lens_s=stones.size();
        //int mark=0;
        int ans=0;
        for(int i=0;i<lens_j;i++)
        {
            for(int j=0;j<lens_s;j++)
            {
                if(jewels[i]==stones[j])
                    ans++;
            }
        }
        return ans;
    }
};