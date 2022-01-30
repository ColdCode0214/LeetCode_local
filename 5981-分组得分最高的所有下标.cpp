class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        int lens=nums.size();
        vector<int> ans;
        ans.push_back(0);
        if(lens==1)
        {
            if(nums[0]==1)
                return ans;
            else
            {
                ans.clear();
                ans.push_back(1);
                return ans;
            }
        }
            
        int sum0=0, sum1=0;
        for(int i=0;i<lens;i++)
        {
            if(nums[i]==0)
                sum0++;
            else
                sum1++;
        }
        //int left=0, right=sum1;
        int score=sum1;
        //cout<<"score:"<<score<<endl;
        
        int temp=score;
        for(int i=1;i<lens;i++)
        {
            if(nums[i-1]==0)
                score++;
            else
                score--;
            //cout<<"score$$$:"<<score<<endl;
            if(score==temp)
                ans.push_back(i);
            else if(score>temp)
            {
                temp=score;
                ans.clear();
                ans.push_back(i);
            }
        }
        if(sum0==temp)
            ans.push_back(lens);
        else if(sum0>temp)
        {
            ans.clear();
            ans.push_back(lens);
        }
        return ans;
    }
};
