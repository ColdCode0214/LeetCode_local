class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int lens=nums.size();
        vector<int> n1, ans;
        int count=0;
        for(int i=0;i<lens;i++)
        {
            if(nums[i]<pivot)
            {
                ans.push_back(nums[i]);
            }
            else if(nums[i]==pivot)
            {
                count++;
            }
            else
            {
                n1.push_back(nums[i]);
            }
        }
        if(count>0)
        {
            for(int i=0;i<count;i++)
                ans.push_back(pivot);
        }
        int lens2=n1.size();

        for(int i=0;i<lens2;i++)
            ans.push_back(n1[i]);
        return ans;
    }
};
