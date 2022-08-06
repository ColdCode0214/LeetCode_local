class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        long long ans=0;
        int lens=nums.size();
        int last=nums[lens-1];
        for(int i=lens-2;i>=0;i--)
        {
            if(nums[i]<=last)
                last=nums[i];
            else
            {
                // float x = nums[i];
                // float temp_last = last;
                // float k=x/temp_last;
                // cout<<"k:"<<k<<endl;
                // k = int(ceil(k));
                int k = (nums[i] + last - 1) / last; //C++中对于被除数与除数都是int型但商想向上取整时的巧妙方法
                ans+=k-1;
                last=nums[i]/k;
            }
        }
        return ans;
    }
};
