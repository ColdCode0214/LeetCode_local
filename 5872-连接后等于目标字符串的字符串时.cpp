class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        int lens_t=target.size();
        int lens_n=nums.size();
        int lens[lens_n];//�洢ÿ���ַ��ĳ��ȣ���Ҫ���ӳɹ�������Ҫλ��һ��
        int count=0;
        for(int i=0;i<lens_n;i++)
            lens[i]=nums[i].size();
        for(int i=0;i<lens_n;i++)
        {
            for(int j=0;j<lens_n;j++)
            {
                if(i!=j && lens[i]+lens[j]==lens_t)
                {
                    if(nums[i]+nums[j]==target)
                        count++;
                }
            }
        }
        return count;
    }
};
