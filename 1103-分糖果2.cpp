class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> ans;
        int num[num_people];
        for(int i=0;i<num_people;i++)
            num[i]=0;
        int count=1;
        while(candies>0)
        {
            if(candies>=count)
            {
                num[(count-1)%num_people]+=count;
                candies-=count;
            }
            else
            {
                num[(count-1)%num_people]+=candies;
                candies=0;
            }
            count++;
        }
        for(int i=0;i<num_people;i++)
            ans.push_back(num[i]);
        return ans;
    }
};
