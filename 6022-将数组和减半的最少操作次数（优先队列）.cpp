class Solution {
public:
    int halveArray(vector<int>& nums) {
        long long int ans=0;
        int lens=nums.size();
        priority_queue<float> q;
        float sum=0;
        for(int i=0;i<lens;i++)
        {
            q.push(nums[i]);
            sum+=nums[i];
        }
        float half=sum/2;
        float div=0;
        while(div<half)
        {
            float temp=q.top();
            q.pop();
            div+=(temp/2);
            q.push(temp/2);
            ans++;
        }
        return ans;
    }
};
