class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int count=0;
        int lens=nums.size();
        int temp=0;
        if(lens==1)
            return true;
        for(int i=0;i<lens-1;i++)
        {
            if(nums[i]>nums[i+1])
            {
                count++;
                if(count>=2)
                    return false;
                temp=nums[i];
                nums[i]=nums[i+1];
                if(is_sorted(nums.begin(), nums.end()))
                    return true;
                nums[i]=temp;
                nums[i+1]=nums[i];//����ÿ����������ԣ����������޸ķ�ʽ��һ���ǽ�ǰһ����ֵ��Ϊ��һ������һ���ǽ���һ����ֵ��Ϊǰһ��
                if(is_sorted(nums.begin(), nums.end()))
                    return true;
            }
        }
        return true;
    }
};
